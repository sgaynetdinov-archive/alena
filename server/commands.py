import asyncio

from .cache import get_cache, CacheKeyNotFound
from .task import Task

cache = get_cache()

command_items = {}

def command(command_name):
    def decorator(func):
        command_items[command_name] = func
        def wrap(*args, **kwargs):
            return func(*args, **kwargs)
        return wrap
    return decorator

@command("create_task")
def create_task():
    pass

@command("status_task")
async def status_task(task_uuid):
    try:
        task_as_dict = await cache.get(task_uuid)
        task = Task.from_dict(task_as_dict)
        return task.status
    except CacheKeyNotFound:
        return "не найдено"

@command("result_task")
def result_task():
    pass

async def is_valid_command(command_name):
    if command_name in command_items:
        return True
    return False

