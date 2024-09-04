# Note: This repository has been archived
This image set was developed under a previous phase of the Yale Digital Humanities Lab. Now a part of Yale Library’s Computational Methods and Data department, the Lab no longer includes this image set in its scope of work. As such, it will receive no further updates.


# Image Datasets

A module of sample image datasets for computer vision projects in Python.

## Installation

To install this module, type in a terminal:

```bash
pip install image_datasets
```

## Usage

To list all available datasets:

```python
import image_datasets
image_datasets.list() # returns a list of datasets ['oslo', 'bain', ...]
```

To download the "bain" dataset:

```python
import image_datasets
image_datasets.bain.download()
```

To load the images in a dataset into RAM at a constant size:

```python
import image_datasets
X = image_datasets.bain.load()
```
