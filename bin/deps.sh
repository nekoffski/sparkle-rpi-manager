#!/bin/bash

sudo apt-get install -y python3.7
sudo apt-get install -y python3-setuptools
sudo apt-get install -y python3.7-venv

sudo python3.7 -m ensurepip
sudo python3.7 -m pip install virtualenv