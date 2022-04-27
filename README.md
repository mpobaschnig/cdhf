# CERN Data Handling Framework

## Mattermost

Clone the repository 

```
git clone https://github.com/mpobaschnig/cdhf
```

Create the jupyter notebook file in the root level directory, and put `mmdata.json` in `input/` directory.

In the end it should look like this:
```
.
├── cdhf
│  ├── README.md
│  └── src
│     └── mattermost
│        ├── channel.py
│        ├── channel_member.py
│        ├── channel_member_history_entry.py
│        ├── preprocessor.py
│        ├── team.py
│        └── team_member.py
├── input
│  └── mmdata.json
└── main.ipynb
```

Then include the files in the notebook from the root level

```python
from cdhf.src.mattermost.preprocessor import Preprocessor
from cdhf.src.mattermost.channel import Channel
from cdhf.src.mattermost.channel_member import ChannelMember
from cdhf.src.mattermost.channel_member_history_entry import ChannelMemberHistoryEntry
from cdhf.src.mattermost.team_member import TeamMember
from cdhf.src.mattermost.team import Team
```
