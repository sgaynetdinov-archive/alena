from uuid import uuid4


class CacheKeyNotFound(Exception):
    pass


class CacheAbstract:
    async def add(self, data):
        raise NotImplemented

    async def get(self, key):
        raise NotImplemented


class Cache(CacheAbstract):
    def __init__(self):
        self._cache = {}

    def _get_key(self):
        return str(uuid4())

    async def add(self, data):
        key = self._get_key()
        self._cache[key] = data
        return key

    async def get(self, key):
        try:
            return self._cache[key]
        except KeyError:
            raise CacheKeyNotFound

