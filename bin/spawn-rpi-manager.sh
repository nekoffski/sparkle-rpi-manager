#!/bin/bash

pushd /usr/local/sparkle-rpi-manager

source ./venv/bin/activate
PYTHONPATH=. ./venv/bin/python3.7 ./src/rpi-manager/run.py
