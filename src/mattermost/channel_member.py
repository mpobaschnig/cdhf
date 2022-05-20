class ChannelMember:
    channel_id: int
    user_id: int
    msg_count: int
    mention_count: int

    def __init__(self, channel_id: int, user_id: int, msg_count: int, mention_count: int):
        """AI is creating summary for __init__

        Args:
            channel_id (int): Channel Identifier
            user_id (int): User Identifier
            msg_count (int): Total Message Count of User with user_id in Channel with channel_id
            mention_count (int):  Total Mentions of User with user_id in Channel with channel_id
        """
        self.channel_id = channel_id
        self.user_id = user_id
        self.msg_count = msg_count
        self.mention_count = mention_count
