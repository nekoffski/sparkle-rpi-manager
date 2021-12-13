#!/bin/bash

root_path=/usr/local/sparkle-rpi-manager

if [ -d $root_path ]; then
    echo "$ found already installed sparkle-rpi-manager, removing"
    rm $root_path -rf
fi

echo "$ creating directory" $root_path
mkdir $root_path

echo "$ copying source files"
cp src bin misc version $root_path -r
chmod +x $root_path/bin/*

echo "$ installing deps"
pushd $root_path

./bin/deps.sh
./bin/venv.sh

popd

echo "$ creating symlinks of service files"
ln -sf $root_path/misc/*.service /lib/systemd/system/

echo "$ enablind services"
sudo systemctl daemon-reload

systemctl enable sparkle-rpi-manager.service
systemctl enable sparkle-watcher.service
