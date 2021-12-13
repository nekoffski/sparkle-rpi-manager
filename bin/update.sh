#!/bin/bash

pushd ~

git clone https://github.com/nekoffski/sparkle-rpi-manager.git --single-branch --branch develop srpi
systemctl stop sparkle-rpi-manager
cp ./srpi/src/rpi-manager/* /usr/local/sparkle-rpi-manager/src/rpi-manager -rf
rm srpi -rf

popd

systemctl restart sparkle-rpi-manager
