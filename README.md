# CERN Data Handling Framework

## Introduction ☕️

### Dataset Description

Mattermost is an open-source communication platform similar to slack that is widely used at CERN. The CERN Anonymized Mattermost Dataset includes Mattermost data from January 2018 to November 2021 with 20794 CERN  users, 2367 Mattermost teams, 12773 Mattermost channels, 151 CERN buildings, and 163 CERN  organizational units. The data set states the relationship between Mattermost teams, Mattermost channels, and CERN users, and holds various information such as channel creation, channel deletion times, user channel joining and leave times, and user-specific information such as building and organizational units. To hide identifiable information (e.g. Team Name, User Name, Channel Name, etc.). the dataset was anonymized. The anonymization was done by omitting some attributes, hashing string values, and removing connections between users/teams/channels.

Dataset License: ***CC BY-NC Creative Commons Attribution Non-Commercial Licence***

Dataset Link: CERN Anonymized Mattermost Data | [Zenodo](https://zenodo.org/record/6319684#.YnOMdi8Rr0o)



## Getting Started 🏁


Retrieve Mattermost Data (`mmdata.json`) from [Zenodo](https://zenodo.org/record/6319684#.YnOMdi8Rr0o)

Clone the repository 

```
git clone https://github.com/mpobaschnig/cdhf
```

Create the jupyter notebook (`undefined.ipyb`) file in the root level directory, and put `mmdata.json` in `input/` directory.

In the end it should look like this:
```
..
├── undefined.ipyb
├── input
    └── mmdata.json
├── cdhf
    ├── README.md
    ├── Pipfile
    ├── Pipfile.lock
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

### Install Dependencies 💻
___ 

#### 1. Install [Pipenv](https://pipenv.pypa.io/en/latest/)
---
If you already have Python and pip, you can easily install Pipenv into your home directory:

```sh
$ pip install --user pipenv
```
Or, if you’re using Fedora 28:
```sh
$ sudo dnf install pipenv
```

It’s possible to install Pipenv with Homebrew on MacOS, or with Linuxbrew on Linux systems. However, this is now discouraged, because updates to the brewed Python distribution will break Pipenv, and perhaps all virtual environments managed by it. You’ll then need to re-install Pipenv at least. If you want to give it a try despite this warning, use:

```sh
$ brew install pipenv
```

#### 2. Install Requirements
---

Navigate to cdhf

```sh
$ cd cdhf
```

Install from Pipfile, if there is one:

```sh
$ pipenv install
```


### Working with the Framework and Jupyter Notebooks 💻
___ 

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

## Documentation 🖨️

TBD

## Citation ✍️
If you happen to mention or use this project as part of one of your scientific works, please cite the following paper: **TODO IARIA PAPER**


## Latest publications 📚
* Jakovljevic, I., Gütl, C., Wagner, A. & Nussbaumer A.(2022). Compiling Open Datasets in Context of Large Organizations while Protecting User Privacy and Guaranteeing Plausible Deniability


## Acknowledgements 🙏

We would like to express our gratitude to CERN, for allowing us to publish the dataset as open data and use it for research purposes.



