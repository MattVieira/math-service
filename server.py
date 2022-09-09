"""
Server Setup File
"""

import uvicorn
from starlette.applications import Starlette
from starlette.middleware import Middleware
from scout_apm.async_.starlette import ScoutMiddleware
from router import Router


middleware_list = [
    Middleware(ScoutMiddleware)
]

app = Starlette(debug=False, routes=Router.get_routes(), middleware=middleware_list)


def start_http_server():
    """
    Handle to concentrate the application start
    :return: None
    """
    uvicorn.run(app, host='0.0.0.0')


if __name__ == '__main__':
    start_http_server()
