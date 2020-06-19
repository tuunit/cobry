#!/usr/bin/env bash

source venv/bin/activate 

rm -rf dist build cobry.egg-info 

python setup.py sdist bdist_wheel

if twine check dist/*; then
    pip install dist/*.tar.gz
fi

rm -rf dist build cobry.egg-info 
