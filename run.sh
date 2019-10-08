#!/bin/bash
#TeamCity

pip install virtualenv
virtualenv --no-site-packages TestEnv
mkdir tmp
source TestEnv/bin/activate
pip install -r requirements.txt
pytest test/authentication.py
deactivate