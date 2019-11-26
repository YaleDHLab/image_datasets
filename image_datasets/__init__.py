from image_datasets.datasets import oslo, bain, list_all
import sys

setattr(sys.modules[__name__], 'list', list_all)