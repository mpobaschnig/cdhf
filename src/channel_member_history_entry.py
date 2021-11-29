from typing import Optional


class ChannelMemberHistoryEntry:
    channel_id: str
    user_id: str
    join_time: int
    leave_time: Optional[int]

    def __init__(self, channel_id: str, user_id: str, join_time: int, leave_time: Optional[int]):
        self.channel_id = channel_id
        self.user_id = user_id
        self.join_time = join_time
        self.leave_time = leave_time
