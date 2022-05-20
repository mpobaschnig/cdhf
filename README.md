# CERN Data Handling Framework

## Introduction ☕️

### Dataset Description

Mattermost is an open-source communication platform similar to slack that is widely used at CERN. The CERN Anonymized Mattermost Dataset includes Mattermost data from January 2018 to November 2021 with 20794 CERN  users, 2367 Mattermost teams, 12773 Mattermost channels, 151 CERN buildings, and 163 CERN  organizational units. The data set states the relationship between Mattermost teams, Mattermost channels, and CERN users, and holds various information such as channel creation, channel deletion times, user channel joining and leave times, and user-specific information such as building and organizational units. To hide identifiable information (e.g. Team Name, User Name, Channel Name, etc.), the dataset was anonymized. The anonymization was done by omitting some attributes, hashing string values, and removing connections between users/teams/channels.

Dataset License: ***CC BY-NC Creative Commons Attribution Non-Commercial Licence***

Dataset Link: CERN Anonymized Mattermost Data | [Zenodo](https://zenodo.org/record/6319684#.YnOMdi8Rr0o)

```bibtex
@dataset{jakovljevic_igor_2022_6319684,
  author       = {Jakovljevic, Igor and
                  Wagner, Andreas and
                  Gütl, Christian and
                  Pobaschnig, Martin and
                  Mönnich, Adrian},
  title        = {CERN Anonymized Mattermost Data},
  month        = mar,
  year         = 2022,
  publisher    = {Zenodo},
  version      = 1,
  doi          = {10.5281/zenodo.6319684},
  url          = {https://doi.org/10.5281/zenodo.6319684}
}

```

---

## Getting Started 🏁


### Setup Repository 💻
---

#### 1. Clone the repository 
---

```
git clone https://github.com/mpobaschnig/cdhf
```


#### 2. Retrieving the Dataset
---
Retrieve Mattermost Data (`mmdata.json`) from [Zenodo](https://zenodo.org/record/6319684#.YnOMdi8Rr0o). To retrieve the dataset execute:
```sh
$ ./init.sh
```
Or, you can manually create the `input/` directory in the root folder, then download the [mmdata.json](https://zenodo.org/record/6319684/files/mattermost.json) into the `input` directory.

#### 3. Jupyter Notebook
---

Create the jupyter notebook (`undefined.ipyb`) file in the root level directory.


#### 4. Conclusion
---
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
---

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
---

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

---


## Citation ✍️

If you happen to mention or use this project as part of one of your scientific works, please cite the following paper: **TODO IARIA PAPER**

---

## Latest publications 📚
* Jakovljevic, I., Gütl, C., Wagner, A. and Nussbaumer, A. Compiling Open Datasets in Context of Large Organizations while Protecting User Privacy and Guaranteeing Plausible Deniability. In Proceedings of the 11th International Conference on Data Science, Technology and Applications (DATA 2022)


```bibtex
@ARTICLE {,
    author  = "Jakovljevic, I., Gütl, C., Wagner, A. and Nussbaumer, A.",
    title   = "Compiling Open Datasets in Context of Large Organizations while Protecting User Privacy and Guaranteeing Plausible Deniability",
    journal = "In Proceedings of the 11th International Conference on Data Science, Technology and Applications (DATA 2022)",
    year    = "2022"
}
```
---

## Involved institutions 🏫
Contributors from the following institutions were involved in the development of this project:
* [CERN](https://home.cern/)
* [Graz University of Technology](https://www.tugraz.at/home/)
---

## 	Visual Exploration & Analysis 👁️‍🗨️

In case you would like to visually explore the CERN Mattermost dataset without any programming you can use [Collaboration Spotting X](https://github.com/aleksbobic/csx).

It is a web-based visual network analytics application which includes various convenient features which enable exploration of network datasets on the fly. 

To get started with exploring the CERN Mattermost dataset read the instructions of CSX.

---

## Acknowledgements 🙏

We would like to express our gratitude to CERN, for allowing us to publish the dataset as open data and use it for research purposes.



