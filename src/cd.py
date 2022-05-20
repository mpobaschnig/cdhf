# cd.py
#
# Copyright 2022 Martin Pobaschnig
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http: //www.gnu.org/licenses/>.

from collections import defaultdict
from typing import Dict, List, Optional

import igraph as ig
import networkx as nx
import numpy as np

from config import Config, Stats
import mattermost.preprocessor


class CD:
    preprocessor: Optional[mattermost.preprocessor.Preprocessor] = None
    config: Optional[Config] = None

    g_nx: Optional[nx.Graph] = None
    g_ig: Optional[ig.Graph] = None

    communities = Optional[List[List[int]]]

    stats: Optional[Stats] = None

    def __init__(self, path: Optional[str] = None) -> None:
        if path is None:
            path = "../../input/mmdata.json"
        self.preprocessor = mattermost.preprocessor.Preprocessor(path)
        self.config = Config()
        self.stats = Stats()

        self.g_nx = nx.Graph()

        self.preprocessor.load_all()

    def __calc_channel_tresholds(self) -> None:
        # Here we calculate the channel threshold.
        # If channels are above/below threshold, they will be ignored
        l = []
        for t in self.preprocessor.teams:
            for c in t.channels:
                l.append(len(c.channel_members))

        mean = np.mean(l)
        sd = np.std(l)

        if self.config.thresholds.channel_members_upper == 0:
            self.config.thresholds.channel_members_upper = mean + 3 * sd

        if self.config.thresholds.channel_members_lower == 0:
            self.config.thresholds.channel_members_lower = 2

    def __create_graph(self) -> None:
        # Create the graph by adding an edge between two users
        # if they both belong to the same channel
        def addl(key, val, map):
            l = map.get(key)
            if l is None:
                map[key] = [val]
            else:
                map[key].append(val)
            return map

        # We get all unique team members of a team
        team_member_list: Dict[str, bool] = {}

        for t in self.preprocessor.teams:
            for member in t.team_members:
                team_member_list[member.user_id] = True

        for (i, t) in enumerate(self.preprocessor.teams):
            for channel in t.channels:
                if self.config.thresholds.channel_members_upper is not None:
                    if len(channel.channel_members) > self.config.thresholds.channel_members_upper:
                        continue

                if self.config.thresholds.channel_members_lower is not None:
                    if len(channel.channel_members) < self.config.thresholds.channel_members_lower:
                        continue

                connections = {}

                for member_1 in channel.channel_members:
                    uid1 = member_1.user_id

                    if team_member_list.get(uid1) is not True:
                        continue

                    for member_2 in channel.channel_members:
                        uid2 = member_2.user_id

                        if team_member_list.get(uid2) is not True:
                            continue

                        if uid1 == uid2:
                            continue

                        l1 = connections.get(uid1)
                        if uid1 < uid2 and l1 is not None and uid2 in connections.get(uid1):
                            continue
                        l2 = connections.get(uid2)
                        if uid2 < uid1 and l2 is not None and uid1 in connections.get(uid2):
                            continue

                        if uid1 < uid2:
                            connections = addl(uid1, uid2, connections)
                        else:
                            connections = addl(uid2, uid1, connections)

                        weight = self.g_nx.get_edge_data(uid1, uid2)

                        if weight is None:
                            self.g_nx.add_edge(uid1, uid2, weight=1)
                        else:
                            self.g_nx.add_edge(
                                uid1, uid2, weight=weight.get("weight") + 1)

    def __threshold_remove_nodes(self) -> None:
        # Here we calculate the node degree threshold.
        # If users have above/below threshold, they will be removed
        l = list(dict(self.g_nx.degree()).values())
        l.sort(reverse=True)

        mean = np.mean(l)
        sd = np.std(l)

        if self.config.thresholds.node_degree_upper == 0:
            self.config.thresholds.node_degree_upper = mean + sd * 3

        if self.config.thresholds.node_degree_lower == 0:
            self.config.thresholds.node_degree_lower = 2

        if self.config.thresholds.node_degree_upper is not None:
            self.g_nx.remove_nodes_from([node for node, degree in dict(
                self.g_nx.degree()).items() if degree > self.config.thresholds.node_degree_upper])

        if self.config.thresholds.node_degree_lower is not None:
            self.g_nx.remove_nodes_from([node for node, degree in dict(
                self.g_nx.degree()).items() if degree < self.config.thresholds.node_degree_lower])

        # Remove disconnected graphs if there are any
        largest_component = max(nx.connected_components(self.g_nx), key=len)
        self.g_nx = self.g_nx.subgraph(largest_component)

        self.stats.average_degree = 2*self.g_nx.number_of_edges() / \
            float(self.g_nx.number_of_nodes())
        self.stats.median_degree = l[int(len(l)/2)]
        self.stats.nodes = self.g_nx.number_of_nodes()
        self.stats.edges = self.g_nx.number_of_edges()

    def __find_communities(self) -> None:
        # Find communities by using label propagation
        self.g_ig = ig.Graph.from_networkx(self.g_nx)

        self.communities = self.g_ig.community_label_propagation(
            weights="weight")

        self.stats.modularity = self.communities.modularity

    def find(self) -> None:
        self.__calc_channel_tresholds()
        self.__create_graph()
        self.__threshold_remove_nodes()
        self.__find_communities()

    def get_recommendations(self, channels: List[int]) -> List[int]:
        # Get recommended teams/channels by "joining" some channels (input),
        # check what part of community most neighbors fall in, and check what
        # the most popular teams/channels within these communities are.
        # They are then used for recommendations.

        # We search for all neighbors of the new user, i.e., all
        # users that are part of the same channels
        neighors = []
        for channel_idx in channels:
            channel = self.preprocessor.channels[channel_idx]
            if channel is None:
                continue

            for cm in channel.channel_members:
                neighors.append(cm.user_id)

        # We now how often and in which community the neighbors are in
        m = defaultdict(int)
        for (i, c) in enumerate(self.communities):
            for n in neighors:
                if n in c:
                    m[i] += 1

        communities_list = list(m.items())
        communities_list.sort(reverse=True, key=lambda x: x[1])

        def addl(key, val, map):
            l = map.get(key)
            if l is None:
                map[key] = [val]
            else:
                map[key].append(val)
            return map

        # Map of user_id -> list of teams of the user
        users_teams = {}
        # Map of user_id -> list of channels of the user
        users_channels = {}

        # Find the teams/users a user is in
        for t in self.preprocessor.teams:
            for c in t.channels:
                for cm in c.channel_members:
                    users_channels = addl(
                        cm.user_id, c.channel_id, users_channels)
                    users_teams = addl(cm.user_id, t.team_id, users_teams)

        # Map of community -> [map of team_id -> number of users]
        community_teams = {}
        # Map of community -> [map of channel_id -> number of users]
        community_channels = {}

        # We now try to find which teams/channels the users of each
        # community are part of and count the number of users in them
        for (i, community) in enumerate(self.communities):
            community_team_map = defaultdict(int)
            community_channel_map = defaultdict(int)

            for user_id in community:
                teams = users_teams.get(user_id)
                channels = users_channels.get(user_id)

                if teams is not None:
                    for team_id in teams:
                        community_team_map[team_id] += 1

                if channels is not None:
                    for channel_id in channels:
                        community_channel_map[channel_id] += 1

            community_teams[i] = community_team_map
            community_channels[i] = community_channel_map

        # Unique team set for recommending teams
        recommended_teams = set()
        # Unique team set for recomending channels
        recommended_channels = set()

        # Find teams/channels that most neighbors are in
        for (i, community) in enumerate(communities_list):
            if i == 3:
                break

            m = community_teams.get(i)
            l = list(m.items())
            l.sort(reverse=True, key=lambda x: x[1])
            for (j, (key, val)) in enumerate(l):
                if j == 3:
                    break
                recommended_teams.add(key)

            m = community_channels.get(i)
            l = list(m.items())
            l.sort(reverse=True, key=lambda x: x[1])
            for (j, (key, val)) in enumerate(l):
                if j == 3:
                    break
                recommended_channels.add(key)

        return (list(recommended_teams), list(recommended_channels))
