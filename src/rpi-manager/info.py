import aiofiles

import shell


async def read_hardware() -> str:
    stdout, _ = await shell.execute("cat /sys/firmware/devicetree/base/model")
    return stdout


async def read_version_file() -> str:
    async with aiofiles.open('version', 'r') as f:
        return await f.read()


async def read_os_info() -> str:
    stdout, _ = await shell.execute("uname -orm")
    return stdout


async def get_uptime() -> str:
    stdout, _ = await shell.execute("uptime --pretty")
    return stdout


async def get_running_services() -> str:
    return [
        'sparkle-frontend',
        'sparkle-rpi-manager'
    ]
