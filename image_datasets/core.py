from __future__ import absolute_import
from keras_preprocessing.image.utils import load_img, img_to_array
import requests, os, tarfile, shutil, glob2
import numpy as np

class Dataset:
  def __init__(self, *args, **kwargs):
    '''Create a new dataset object'''
    self.image_path = kwargs.get('image_path', '')
    self.metadata_path = kwargs.get('metadata_path', '')
    self.name = kwargs.get('name', '')
    self.out_dir = os.path.join(os.getcwd(), 'datasets', self.name)
    self.image_extensions = ['.jpg', '.png']

  def download(self, flatten=False, blocksize=10**11):
    '''Download the dataset to local disk'''
    for i in ['metadata', 'images']:
      out_path = os.path.join(self.out_dir, i)
      if not os.path.exists(out_path):
        os.makedirs(out_path)
    # download metadata
    print(' * downloading {} metadata from {}'.format(self.name, self.metadata_path))
    metadata_path = os.path.join(self.out_dir, 'metadata', 'metadata.csv')
    self.save(metadata_path, self.metadata_path, blocksize=blocksize)
    # download the images
    print(' * downloading {} images from {}'.format(self.name, self.image_path))
    image_dir = os.path.join(self.out_dir, 'images')
    image_path = os.path.join(image_dir, '{}.tar'.format(self.name))
    self.save(image_path, self.image_path, blocksize=blocksize)
    # extract from the tar file
    with tarfile.open(image_path) as f: f.extractall(path=image_dir)
    # remove tar file extraction artifacts and flatten result
    for i in glob2.glob(os.path.join(image_dir, '**')):
      if os.path.basename(i).startswith('._'):
        self.delete(i)
      if flatten:
        if any([i.lower().endswith(j) for j in self.image_extensions]):
          shutil.move(i, os.path.join(image_dir, os.path.basename(i)))
    self.delete(image_path)

  def save(self, path, url, blocksize=10**11):
    '''Save the content at `url` locally at `path`'''
    if not os.path.exists(path):
      with open(path, 'wb') as out:
        r = requests.get(url, allow_redirects=True)
        for i in range(0, len(r.content), blocksize):
          out.write(r.content[i:i+blocksize])

  def delete(self, path):
    '''
    Delete a file or directory at path
    '''
    try:
      os.remove(path)
    except:
      shutil.rmtree(path)

  def load(self, size=256, keep_proportions=True):
    '''Load a dataset into RAM at a constant size'''
    X = []
    for i in glob2.glob(os.path.join(self.out_dir, '**')):
      if not any([i.endswith(j) for j in self.image_extensions]): continue
      if os.path.basename(i).startswith('._'): continue
      im = load_img(i)
      if keep_proportions:
        X.append(self.resize_to_square(im, size))
      else:
        X.append(im.resize(size, size))
    return np.array(X)

  def resize_to_height(self, im, height):
    '''Resize `im` into an image with height `height` and proportional width'''
    w,h = im.size
    size = (int(w/h*height), height)
    return img_to_array(im.resize(size))

  def resize_to_max(self, im, n):
    '''
    Resize self.original so its longest side has n pixels (maintain proportion)
    '''
    w,h = im.size
    size = (n, int(n * h/w)) if w > h else (int(n * w/h), n)
    return img_to_array(im.resize(size))

  def resize_to_square(self, im, n, center=True):
    '''Resize `im` to square while maintaining proportion'''
    a = self.resize_to_max(im, n)
    w,h,c = a.shape
    pad_lr = int((n-w)/2) # left right pad
    pad_tb = int((n-h)/2) # top bottom pad
    b = np.zeros((n,n,3))
    if center: b[ pad_lr:pad_lr+w, pad_tb:pad_tb+h, : ] = a
    else: b[:w,:h,:] = a
    return b
