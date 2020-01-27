import ipaddress

import validators
from starlette.exceptions import HTTPException
from validators import ValidationFailure


def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        raise HTTPException(400, 'Invalid IP address.')


def validate_url(url):
    try:
        validators.url(url)
    except ValidationFailure:
        raise HTTPException(400, 'Invalid URL address.')