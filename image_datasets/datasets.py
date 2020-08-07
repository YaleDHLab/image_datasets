from image_datasets.core import Dataset
import sys

hosts = {
  'pixplot': 'http://pixplot.yale.edu/datasets'
}

bain = Dataset(
  name='bain',
  image_path=hosts['pixplot'] + '/bain/photos.tar',
  metadata_path=hosts['pixplot'] + '/bain/metadata.csv',
)

fsaowi_ct = Dataset(
  name='fsaowi_ct',
  image_path=hosts['pixplot'] + '/fsaowi_ct/images.tar',
  metadata_path=hosts['pixplot'] + '/fsaowi_ct/metadata.csv',
)

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

si_open_access = Dataset(
  name='si_open_access',
  image_path=hosts['pixplot'] + '/si-openaccess/images.tar',
  metadata_path=None,
)

def list_all():
  return ['bain', 'fsaowi_ct', 'oslo', 'oslomini', 'si_open_access']
