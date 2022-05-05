# CERN Data Handling Framework

## Mattermost

Request access for Mattermost Data (`mmdata.json`) from [Zenodo](https://zenodo.org/record/6319684#.YnOMdi8Rr0o)

Clone the repository 

```
git clone https://github.com/mpobaschnig/cdhf
```

Create the jupyter notebook file in the root level directory, and put `mmdata.json` in `input/` directory.

In the end it should look like this:
```
..
├── README.md
└── src
    ├── cd.py
    ├── config.py
    ├── example.ipynb
    └── mattermost
        ├── channel_member_history_entry.py
        ├── channel_member.py
        ├── channel.py
        ├── preprocessor.py
        ├── team_member.py
        ├── team.py
        └── user_data.py
```

Then include this file in the notebook from the root level

```python
from cdhf.src.mattermost.preprocessor import Preprocessor
```

Create the preprocessor to work with the data:

```python
p = Preprocessor()

p.load_all()

print(len(p.teams))
```

`cd.py`, `config.py` and `example.py` contain a simple community detection example using the framework.