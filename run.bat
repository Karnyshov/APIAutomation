PYENV_HOME=$WORKSPACE/.pyenv/
virtualenv --no-site-packages %PYENV_HOME%
source %PYENV_HOME}%/bin/activate
pip install -U pytest
pip install -r requirements.txt
pytest test_authentication.py
deactivate