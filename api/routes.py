from starlette.routing import Route, Mount

from api.views import ip_object_handler, url_object_handler

ROUTES = [
    Mount('/ip', routes=[
        Route('/', ip_object_handler, name='get_ips', methods=['GET']),
        Route('/{ip_address}', ip_object_handler, name='get_ip', methods=['GET', 'POST', 'DELETE']),
    ]),
    Mount('/url', routes=[
        Route('/', url_object_handler, name='get_urls', methods=['GET']),
        Route('/{url_address}', url_object_handler, name='get_url', methods=['GET', 'POST', 'DELETE']),
    ]),
]
