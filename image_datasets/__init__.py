from image_datasets.datasets import *
import sys

setattr(sys.modules[__name__], 'list', list_all)
