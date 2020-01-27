from starlette.applications import Starlette
from starlette.routing import Mount

from api.db import database
from api.routes import ROUTES

app = Starlette(
    routes=[
        Mount('/', routes=ROUTES),
    ],
    on_startup=[database.connect],
    on_shutdown=[database.disconnect]
)
