from typing import Optional


class ChannelMemberHistoryEntry:
    channel_id: int
    user_id: int
    join_time: int
    leave_time: Optional[int]

    def __init__(self, channel_id: int, user_id: int, join_time: int, leave_time: Optional[int]):
        """

        Args:
            channel_id (int): Channel Identifier
            user_id (int): User Identifier
            join_time (int): Timestamp when the user with user_id joined the chennel with the channel_id
            leave_time (Optional[int]): Timestamp when the user with user_id left the chennel with the channel_id
        """
        self.channel_id = channel_id
        self.user_id = user_id
        self.join_time = join_time
        self.leave_time = leave_time
