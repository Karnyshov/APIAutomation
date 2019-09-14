mkdir pyenv
PYENV_HOME=$WORKSPACE\pyenv\
venv my_env --no-site-packages %PYENV_HOME%
source %PYENV_HOME%\Scripts\activate.bat
pip install -r requirements.txt
pytest test_authentication.py
deactivate