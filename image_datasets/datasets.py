from image_datasets.core import Dataset
import sys

hosts = {
  'pixplot': 'http://pixplot.yale.edu/datasets'
}

oslo = Dataset(
  name='oslo',
  image_path=hosts['pixplot'] + '/oslo/photos.tar',
  metadata_path=hosts['pixplot'] + '/oslo/metadata.csv',
)

bain = Dataset(
  name='bain',
  image_path=hosts['pixplot'] + '/bain/photos.tar',
  metadata_path=hosts['pixplot'] + '/bain/metadata.csv',
)

def list_all():
  return ['oslo', 'bain']