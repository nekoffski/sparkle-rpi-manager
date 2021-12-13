
import asyncio

from sanic import Sanic
from sanic_cors import CORS

from endpoint import setup_endpoints


app = Sanic("RPI Manager")
CORS(app)


setup_endpoints(app)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    try:
        app.run(host='0.0.0.0', port=5555)
    finally:
        loop.close()
