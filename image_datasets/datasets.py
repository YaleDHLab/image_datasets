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

oslomini = Dataset(
  name='oslomini',
  image_path=hosts['pixplot'] + '/oslomini/photos.tar',
  metadata_path=hosts['pixplot'] + '/oslomini/metadata.csv',
)

fsaowi_ct = Dataset(
  name='fsaowi_ct',
  image_path=hosts['pixplot'] + '/fsaowi_ct/images.tar',
  metadata_path=hosts['pixplot'] + '/fsaowi_ct/metadata.csv',
)

bain = Dataset(
  name='bain',
  image_path=hosts['pixplot'] + '/bain/photos.tar',
  metadata_path=hosts['pixplot'] + '/bain/metadata.csv',
)

def list_all():
  return ['oslo', 'oslomini', 'bain']
