import time
import os
import actions


WATCHER_DIR = '/usr/local/sparkle-rpi-manager'
EVENTS_DIR = f'{WATCHER_DIR}/events'


def observe_events():
    def get_event_files():
        return [f for f in os.listdir(EVENTS_DIR)]

    delay = 0.5

    if not os.path.isdir(EVENTS_DIR):
        os.mkdir(EVENTS_DIR)

    while True:
        for file in get_event_files():
            event = file.split('.')[0]

            print(f"$ Processing event: {file}")

            if event not in actions.actions:
                print(f"WARNING: unknown event file: {file}")
                continue

            os.remove(os.path.join(EVENTS_DIR, file))
            actions.actions[event]()
        print(f"$ Sleeping {delay}")
        time.sleep(delay)


if __name__ == '__main__':
    observe_events()
