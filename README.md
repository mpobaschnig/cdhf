# CERN Data Handling Framework

## Introduction ☕️

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

#### Install [Pipenv](https://pipenv.pypa.io/en/latest/)
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

#### Install Requirements
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


## Citation ✍️
If you happen to mention or use this project as part of one of your scientific works, please cite the following paper: **TODO IARIA PAPER**


## Latest publications 📚
* Jakovljevic, I., Gütl, C., Wagner, A. & Nussbaumer A.(2022). Compiling Open Datasets in Context of Large Organizations while Protecting User Privacy and Guaranteeing Plausible Deniability

