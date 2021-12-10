import asyncio

from sanic import Sanic
from sanic.response import json

app = Sanic("RPI Manager")


@app.post('/run/')
async def post_run(request):
    command = request.json["command"]

    proc = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()

    return json({
        "stdout": stdout.decode(),
        "stderr": stderr.decode()
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
