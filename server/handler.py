import asyncio

from .cache import get_cache, CacheKeyNotFound
from .task import Task
from .status import Status
from .queue import get_queue

cache = get_cache()
queue = get_queue()

handler_items = {}

def register_handler(handler_name):
    def decorator(func):
        handler_items[handler_name] = func
        def wrap(*args, **kwargs):
            return func(*args, **kwargs)
        return wrap
    return decorator

@register_handler("create_task")
async def create_task(command):
    task = Task(command=command, status=Status.QUEUE)
    task_uuid = await cache.add(task.as_dict())
    await queue.put(task.as_dict())
    return task_uuid

@register_handler("status_task")
async def status_task(task_uuid):
    try:
        task_as_dict = await cache.get(task_uuid)
        task = Task.from_dict(task_as_dict)
        return task.status.value
    except CacheKeyNotFound:
        return "не найдено"

@register_handler("result_task")
async def result_task(task_uuid):
    try:
        task_as_dict = await cache.get(task_uuid)
        task = Task.from_dict(task_as_dict)
    except CacheKeyNotFound:
        return "не найдено"
    
    if task.status != Status.COMPLETED:
        return "не найдено"

    return task.result

async def handler(command):
    handler_name, *args = command.split()
    try:
        func = handler_items[handler_name]
        return await func(*args)
    except KeyError:
        return "неверная команда"

