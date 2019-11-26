from setuptools import setup

setup (
  name='image_datasets',
  version='0.0.1',
  packages=['image_datasets'],
  keywords = ['computer-vision', 'machine-learning', 'datasets'],
  description='Image datasets for computer vision projects',
  url='https://github.com/yale-dhlab/image_datasets',
  author='Douglas Duhaime',
  author_email='douglas.duhaime@gmail.com',
  license='MIT',
  install_requires=[
    'glob2>=0.6',
    'numpy>=1.12.0',
    'requests>=2.22.0',
    'yale-dhlab-keras-preprocessing>=1.1.1',
  ],
)