from starlette.applications import Starlette
from starlette.routing import Mount

from api.routes import ROUTES

app = Starlette(routes=[
    Mount('/v1', routes=ROUTES)
])