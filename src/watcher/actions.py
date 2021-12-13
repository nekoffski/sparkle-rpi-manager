import os


actions = {
    "reboot": lambda: os.system('sleep 1; sudo reboot'),
    "update": lambda: os.system('sleep 1; sudo /usr/local/sparkle-rpi-manager/bin/update.sh')
}
