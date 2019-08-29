import asyncio

class QueueAbstract:
    async def pop(self):
        raise NotImplemented

    async def put(self, item):
        raise NotImplemented

    async def size(self):
        raise NotImplemented


class Queue:
    instance = None

    def __init__(self):
        self._queue = asyncio.Queue()

    async def pop(self):
        return await self._queue.get()

    async def put(self, item):
        return await self._queue.put(item)

    async def size(self):
        return self._queue.qsize()


def get_queue():
    if Queue.instance is None:
        Queue.instance = Queue()

    return Queue.instance

