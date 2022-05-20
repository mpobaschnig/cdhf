# config.py
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

from typing import Dict, List, Optional, Tuple
from enum import Enum


class Thresholds:
    # 0 is automatic detection of thresholds
    node_degree_upper: Optional[int] = 0
    node_degree_lower: Optional[int] = 0
    channel_members_upper: Optional[int] = 0
    channel_members_lower: Optional[int] = 0


class AlgorithmType(Enum):
    ASYN_LPA_COMMUNYTIES = 0


class Config:
    thresholds: Thresholds = Thresholds()

    # Algorithm to run, can be: "greedy_modularity", "asyn_lpa_communities"
    algo: AlgorithmType = AlgorithmType.ASYN_LPA_COMMUNYTIES


class Stats:
    nodes: int
    edges: int

    average_degree: float
    median_degree: float

    modularity: float
