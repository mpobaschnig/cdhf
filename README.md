# CERN Data Handling Framework

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6575935.svg)](https://doi.org/10.5281/zenodo.6575935)

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


### Setup 💻
---

#### 1. Retrieving the Dataset
---
Retrieve Mattermost Data (`mmdata.json`) from [Zenodo](https://zenodo.org/record/6319684#.YnOMdi8Rr0o).

#### 2. Install cdhf from pypi
---

Install the cdhf package by

```sh
$ pip install cdhf
```

#### 3. Import and use cdhf
---

Include the cdhf package:

```python
from cdhf.data import Data
```

Create the Data object to and load the data set:

```python
data = Data("path/to/mmdata.json/file")

data.load_all()
```

You can find examples on how to work with the data at the [cdhf-examples](https://github.com/mpobaschnig/cdhf-examples) repository.

## Documentation 🖨️

API documentation is available at [https://mpobaschnig.github.io/cdhf/](https://mpobaschnig.github.io/cdhf/).

---


## Citation ✍️

If you happen to mention or use this project as part of one of your scientific works, please cite the following paper: 

* Jakovljevic, I., Pobaschnig, M., Gütl, C. and Wagner, A., 2022. Privacy Aware Identification of User Clusters in Large Organisations based on Anonymized Mattermost User and Channel Information. In: DATA ANALYTICS 2021, The Tenth International Conference on Data Analytics.

```bibtex

@inproceedings{DataAnalytics2022,
  author  = { Jakovljevic, I., Pobaschnig, M., Gütl, C. AND Wagner, A. },
  year    = { 2022 },
  month   = { 11 },
  title   = { Privacy Aware Identification of User Clusters in Large Organisations based on Anonymized Mattermost User and Channel Information }
}

```

---

## Latest publications 📚
* Jakovljevic, I., Gütl, C., Wagner, A. and Nussbaumer, A. Compiling Open Datasets in Context of Large Organizations while Protecting User Privacy and Guaranteeing Plausible Deniability. In Proceedings of the 11th International Conference on Data Science, Technology and Applications (DATA 2022)


```bibtex

@article{Data2022,
    author  = { Jakovljevic, I., Gütl, C., Wagner, A. and Nussbaumer, A. },
    title   = { Compiling Open Datasets in Context of Large Organizations while Protecting User Privacy and Guaranteeing Plausible Deniability },
    journal = { In Proceedings of the 11th International Conference on Data Science, Technology and Applications (DATA 2022) },
    year    = { 2022 }
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



