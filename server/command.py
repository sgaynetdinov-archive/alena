import asyncio

command_items = {}

def register_command(command_name):
    def decorator(func):
        command_items[command_name] = func
        def wrap(*args, **kwargs):
            return func(*args, **kwargs) 
        return wrap
    return decorator

@register_command("reversed_string")
async def reversed_string():
    await asyncio.sleep(3)

@register_command("transposition")
async def transposition():
    await asyncio.sleep(7)

