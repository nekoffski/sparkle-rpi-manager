import os
import typing

from pathlib import Path


def create_event_file(name: str) -> typing.NoReturn:
    events_dir = '/usr/local/sparkle-rpi-manager/events'
    Path(os.path.join(events_dir, name + '.event')).touch()


EVENT_REBOOT = 'reboot'
EVENT_UPDATE = 'update'
