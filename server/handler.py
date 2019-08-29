import asyncio
from uuid import uuid4

from .cache import get_cache, CacheKeyNotFound
from .task import Task
from .status import Status
from .queue import get_queue
from .command import command_items

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
    if command not in command_items:
        return "неверная команда"

    key = str(uuid4())
    task = Task(command=command, status=Status.QUEUE.value, uuid=key)
    task_uuid = await cache.add(key, task.as_json())
    await queue.put(task.as_json())
    return task_uuid

@register_handler("status_task")
async def status_task(task_uuid):
    try:
        task_as_dict = await cache.get(task_uuid)
        task = Task.from_json(task_as_dict)
        return task.status
    except CacheKeyNotFound:
        return "не найдено"

@register_handler("result_task")
async def result_task(task_uuid):
    try:
        task_as_dict = await cache.get(task_uuid)
        task = Task.from_json(task_as_dict)
    except CacheKeyNotFound:
        return "не найдено"
    
    if task.status != Status.COMPLETED.value:
        return "не найдено"

    return task.result

async def handler(command):
    handler_name, *args = command.split()
    try:
        func = handler_items[handler_name]
        return await func(*args)
    except KeyError:
        return "неверная команда"

