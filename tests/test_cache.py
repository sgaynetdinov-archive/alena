import pytest

from server.cache import Cache, CacheKeyNotFound, get_cache

@pytest.fixture
def cache():
    return Cache()

@pytest.mark.asyncio
async def test_cache(cache):
    assert await cache.add('100500', 'Payload') == '100500'
    assert await cache.get('100500') == 'Payload'


@pytest.mark.asyncio
async def test_not_found_key(cache):
    with pytest.raises(CacheKeyNotFound):
        await cache.get('100500')


def test_get_cache_is_singelton():
    cache = get_cache()
    assert cache is get_cache() 
