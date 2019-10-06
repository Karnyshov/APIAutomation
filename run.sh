#!/bin/bash
#TeamCity

pip install virtualenv
venv --no-site-packages TestEnv
PYENV_HOME=/TestEnv
source $PYENV_HOME/bin/activate
pip install -r requirements.txt
pytest test_authentication.py
deactivate