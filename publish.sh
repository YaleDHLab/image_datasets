# your ~/.pypirc must be configured
rm -rf dist/
rm -rf image_datasets.egg-info
python -m build
twine upload dist/*
