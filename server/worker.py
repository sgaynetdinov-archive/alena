import asyncio

from server.queue import get_queue
from server.command import command_items
from server.task import Task
from server.status import Status
from server.cache import get_cache

cache = get_cache()
queue = get_queue()

def worker():
    return asyncio.run(_worker())

async def _worker():
    while True:
        if await queue.size() == 0:
            continue

        item = await queue.pop()
        task = Task.from_json(item)
        task.status = Status.IN_PROGRESS.value 
        await cache.add(task.uuid, task.as_json())

        command, *args = task.command.split()
        func = command_items[command] 
        got = await func(*args)

        task.status = Status.COMPLETED.value
        task.result = got
        await cache.add(task.uuid, task.as_json())

