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
