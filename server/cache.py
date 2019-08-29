class CacheKeyNotFound(Exception):
    pass


class CacheAbstract:
    instance = None

    async def add(self, data):
        raise NotImplemented

    async def get(self, key):
        raise NotImplemented


class Cache(CacheAbstract):
    def __init__(self):
        self._cache = {}

    async def add(self, key, data):
        self._cache[key] = data
        return key

    async def get(self, key):
        try:
            return self._cache[key]
        except KeyError:
            raise CacheKeyNotFound


def get_cache():
    if not Cache.instance:
        Cache.instance = Cache() 

    return Cache.instance

