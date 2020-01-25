from api.actions import get_ip, create_ip, delete_ip, get_url, create_url, delete_url

IP_ACTIONS = {
    'GET': get_ip,
    'POST': create_ip,
    'DELETE': delete_ip
}

URL_ACTIONS = {
    'GET': get_url,
    'POST': create_url,
    'DELETE': delete_url
}


def get_or_create_ips(request):
    return IP_ACTIONS[request.method](request.query_params.get('ip_address'))


def ip_object_handler(request):
    return IP_ACTIONS[request.method](request.query_params.get('ip_address'))


def get_or_create_urls(request):
    return URL_ACTIONS[request.method](request.query_params.get('url_address'))


def url_object_handler(request):
    return URL_ACTIONS[request.method](request.query_params.get('url_address'))
