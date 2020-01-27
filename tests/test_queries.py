import json

import pytest
from starlette.exceptions import HTTPException

from api.actions import get_ip, create_ip


@pytest.mark.asyncio
async def test_create_ip(event_loop, create_test_database):
    response = await create_ip('127.0.0.2')
    assert json.loads(response.body) == {
        'ip': '127.0.0.2', 'type': None, 'continent_code': None, 'continent_name': None, 'country_code': None,
        'country_name': None, 'region_code': None, 'city': None, 'zip': None, 'latitude': None, 'longitude': None,
        'region_name': None, 'geoname_id': None, 'capital': None, 'language_code': None, 'language_name': None,
        'language_native': None, 'country_flag': None, 'calling_code': None, 'is_eu': None
    }


@pytest.mark.asyncio
async def test_select_all_ips(event_loop, create_test_database):
    response = await get_ip(None)
    assert json.loads(response.body) == [
        {
            'ip': '127.0.0.2', 'type': None, 'continent_code': None, 'continent_name': None, 'country_code': None,
            'country_name': None, 'region_code': None, 'city': None, 'zip': None, 'latitude': None, 'longitude': None,
            'region_name': None, 'geoname_id': None, 'capital': None, 'language_code': None, 'language_name': None,
            'language_native': None, 'country_flag': None, 'calling_code': None, 'is_eu': None
        }
    ]


@pytest.mark.asyncio
async def test_select_ip(event_loop, create_test_database):
    with pytest.raises(HTTPException):
        await get_ip('127.0.0.1')
