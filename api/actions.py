from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse

from api.db import ips, database, urls
from api.validators import validate_ip, validate_url


async def get_ip(ip_address):
    if not ip_address:
        return JSONResponse(
            [
                dict(result) for result in await database.fetch_all(ips.select())
            ]
        )
    validate_ip(ip_address)
    result = await database.fetch_one(ips.select(ips.c.ip == ip_address))
    if not result:
        raise HTTPException(404, 'IP address not found.')
    return JSONResponse(dict(result))


async def create_ip(ip_address):
    validate_ip(ip_address)
    # TODO IpStack Handler to get IP geoloc data
    # TODO build object from IpStack data
    try:
        await database.execute(ips.insert().values(ip=ip_address))
        return await get_ip(ip_address)
    except Exception:
        raise HTTPException(400, 'Duplicated IP address.')


async def delete_ip(ip_address):
    validate_ip(ip_address)
    try:
        await database.execute(ips.delete(ips.c.ip == ip_address))
        return JSONResponse('IP has been Successfully deleted.')
    except:
        raise HTTPException(400, 'IP does not exist.')


async def get_url(url_address):
    if not url_address:
        return database.fetch_all(urls.select())
    validate_url(url_address)
    return JSONResponse(await database.fetch_one(urls.select(urls.c.url == url_address)))


async def create_url(url_address):
    validate_url(url_address)
    # TODO IpStack Handler to get url geoloc data
    # TODO build object from IpStack data
    await database.execute(urls.insert().values(url=url_address))
    return get_url(url_address)


async def delete_url(url_address):
    validate_url(url_address)
    await database.execute(urls.delete(urls.c.url == url_address))
    return JSONResponse('URL has been Successfully deleted.')
