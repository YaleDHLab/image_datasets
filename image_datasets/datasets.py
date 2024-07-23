from image_datasets.core import Dataset
import sys

hosts = {
  'pixplot': 'http://pixplot.yale.edu/datasets',
  'duhaime': 'https://duhaime.s3.amazonaws.com/yale-dh-lab/image-datasets'
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
  image_path=hosts['duhaime'] + '/oslo/images.tar',
  metadata_path=hosts['duhaime'] + '/oslo/metadata.csv',
)

oslomini = Dataset(
  name='oslomini',
  image_path=hosts['duhaime'] + '/oslomini/images.tar',
  metadata_path=hosts['duhaime'] + '/oslomini/metadata.csv',
)

si_open_access = Dataset(
  name='si_open_access',
  image_path=hosts['pixplot'] + '/si-openaccess/images.tar',
  metadata_path=None,
)

ycba = Dataset(
  name='ycba',
  image_path=hosts['pixplot'] + '/ycba/images.tar',
  metadata_path=hosts['pixplot'] + '/ycba/metadata.csv',
)

def list_all():
  return ['bain', 'fsaowi_ct', 'oslo', 'oslomini', 'si_open_access']
