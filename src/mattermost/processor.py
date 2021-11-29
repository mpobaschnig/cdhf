import networkx as nx

from typing import Dict, List

from preprocessor import Preprocessor
from channel import Channel
from channel_member import ChannelMember
from channel_member_history_entry import ChannelMemberHistoryEntry
from team_member import TeamMember


class Processor:
    def __init__(self) -> None:
        pass

    def calc_team_graph(self, pp: Preprocessor) -> None:
        pp.teams.sort(reverse=True, key=lambda x: len(x.team_members))

        print("There are {} teams".format(len(pp.teams)))

        for i in range(10):
            print("Team Id {} with {} channels and a total of {} members".format(
                pp.teams[i].team_id,
                len(pp.teams[i].channels),
                len(pp.teams[i].team_members)))
