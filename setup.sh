#!/bin/bash

# Install and setup pyenv
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~./bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc

pyenv install 3.9.0
pyenv global 3.9.0

# Download pip packages
python3.9 -m pip install --upgrade pip
pip install requests
pip install mysql-connector-python


