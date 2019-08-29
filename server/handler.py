import asyncio

from .cache import get_cache, CacheKeyNotFound
from .task import Task
from .status import Status

cache = get_cache()

handler_items = {}

def handler(handler_name):
    def decorator(func):
        handler_items[handler_name] = func
        def wrap(*args, **kwargs):
            return func(*args, **kwargs)
        return wrap
    return decorator

@handler("create_task")
def create_task(command):
    task = Task(command=command, status=Status.QUEUE)
    task_uuid = cache.add(task.as_dict())
    return task_uuid

@handler("status_task")
async def status_task(task_uuid):
    try:
        task_as_dict = await cache.get(task_uuid)
        task = Task.from_dict(task_as_dict)
        return task.status
    except CacheKeyNotFound:
        return "не найдено"

@handler("result_task")
async def result_task(task_uuid):
    try:
        task_as_dict = await cache.get(task_uuid)
        task = Task.from_dict(task_as_dict)
    except CacheKeyNotFound:
        return "не найдено"
    
    if task.status != Status.COMPLETED:
        return "не найдено"

    return task.result

async def is_valid_handler(handler_name):
    if handler_name in handler_items:
        return True
    return False
