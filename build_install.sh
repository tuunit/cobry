#!/usr/bin/env bash

echo -e "\n====== Activate venv ======\n"
source venv/bin/activate 

rm -rf dist build cobry.egg-info 

echo -e "\n======= Build corby =======\n"
python setup.py sdist bdist_wheel

echo -e "\n====== Install corby ======\n"
pip install dist/*.tar.gz

echo -e "\n======== Clean up =========\n"
rm -rf dist build cobry.egg-info 
