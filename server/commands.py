import asyncio

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
def status_task():
    pass

@command("result_task")
def result_task():
    pass

async def is_valid_command(command_name):
    if command_name in command_items:
        return True
    return False

