from typing import List, Optional

from .channel_member import ChannelMember
from .channel_member_history_entry import ChannelMemberHistoryEntry


class Channel:
    """ Class Representing Channel Information
    """
    channel_id: int
    team_id: int
    creator_id: int
    create_at: int
    delete_at: int
    total_msg_count: int
    post_count: int
    reactions_count: int

    # Custom stuff
    channel_members: List[ChannelMember]
    channel_member_history: List[ChannelMemberHistoryEntry]

    def __init__(self, channel_id: int, team_id: int, creator_id: int, create_at: int, delete_at: int, total_msg_count: int, post_count: int, reactions_count: int, channel_members: List[ChannelMember], channel_member_history: List[ChannelMemberHistoryEntry]):
        """

        Args:
            channel_id (int): Channel Identifier
            team_id (int): Team Identifier
            creator_id (int): Creator User Identifier
            create_at (int): Created Timestamp
            delete_at (int): Deleted Timestamp
            total_msg_count (int): Total Channel Message Count
            post_count (int): Total Channel Post Count
            reactions_count (int): Total CHannel Reactions Count
            channel_members (List[ChannelMember]): List of Channel Members
            channel_member_history (List[ChannelMemberHistoryEntry]): List that contains information when users joined of left the Channel
        """
        self.channel_id = channel_id
        self.team_id = team_id
        self.creator_id = creator_id
        self.create_at = create_at
        self.delete_at = delete_at
        self.total_msg_count = total_msg_count
        self.post_count = post_count
        self.reactions_count = reactions_count

        # Custom stuff
        self.channel_members = channel_members
        self.channel_member_history = channel_member_history
