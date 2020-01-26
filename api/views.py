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


async def ip_object_handler(request):
    return await IP_ACTIONS[request.method](request.path_params.get('ip_address'))


async def url_object_handler(request):
    return await URL_ACTIONS[request.method](request.path_params.get('url_address'))
