import asyncio

from sanic.response import json, text

import info
import shell
import event


def setup_endpoints(app):
    @app.post('/update')
    async def post_update(_):
        event.create_event_file(event.EVENT_UPDATE)

        return text("Update scheduled")

    @app.post('/reboot')
    async def post_reboot(_):
        event.create_event_file(event.EVENT_REBOOT)

        return text("Reboot scheduled")

    @app.get('/ping')
    async def get_ping(_):
        return text("pong")

    @app.get('/')
    async def get_root(_):
        hardware, version, os, uptime, services = await asyncio.gather(
            info.read_hardware(),
            info.read_version_file(),
            info.read_os_info(),
            info.get_uptime(),
            info.get_running_services()
        )

        return json({
            "hardware": hardware,
            "software": f"sparkle-rpi-manager-{version}",
            "os": os,
            "uptime": uptime,
            "services": services
        })

    @app.post('/run/')
    async def post_run(request):
        command = request.json["command"]

        stdout, stderr = await shell.execute(command)

        return json({
            "stdout": stdout,
            "stderr": stderr
        })
