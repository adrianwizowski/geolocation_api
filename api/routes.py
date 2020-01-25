from starlette.routing import Route, Mount

from api.views import get_or_create_ips, ip_object_handler, get_or_create_urls, url_object_handler

ROUTES = [
    Mount('/ip', routes=[
        Route('/ip', get_or_create_ips, name='get_ips', methods=['GET', 'POST']),
        Route('/ip/{ip_address}', ip_object_handler, name='get_ip', methods=['GET', 'DELETE']),
    ]),
    Mount('/url', routes=[
        Route('/url', get_or_create_urls, name='get_urls', methods=['GET', 'POST']),
        Route('/url/{url_address}', url_object_handler, name='get_ip', methods=['GET', 'DELETE']),
    ]),
]
