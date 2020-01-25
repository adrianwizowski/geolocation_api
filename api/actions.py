from api.db import ips, database, urls
from api.validators import validate_ip, validate_url


def get_ip(ip_address):
    if not ip_address:
        return database.fetch_all(ips.select())
    validate_ip(ip_address)
    return database.fetch_one(ips.select(ip=ip_address))


def create_ip(ip_address):
    validate_ip(ip_address)
    return database.execute(ips.insert(ip=ip_address))


def delete_ip(ip_address):
    validate_ip(ip_address)
    return database.execute(ips.delete(ip=ip_address))


def get_url(url_address):
    if not url_address:
        return database.fetch_all(urls.select())
    validate_url(url_address)
    return database.fetch_one(urls.select(url=url_address))


def create_url(url_address):
    validate_url(url_address)
    return database.execute(urls.insert(url=url_address))


def delete_url(url_address):
    validate_url(url_address)
    return database.execute(urls.delete(url=url_address))
