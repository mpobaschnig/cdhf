class ChannelMember:
    channel_id: str
    user_id: str
    msg_count: int
    mention_count: int

    def __init__(self, channel_id: str, user_id: str, msg_count: int, mention_count: int):
        self.channel_id = channel_id
        self.user_id = user_id
        self.msg_count = msg_count
        self.mention_count = mention_count
