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
async def reversed_string(string):
    await asyncio.sleep(3)
    return ''.join(reversed(string))

@register_command("transposition")
async def transposition(string):
    await asyncio.sleep(7)

    got = []
    
    for i in zip(string[1::2], string[::2]):
        got.extend(i)

    if len(string) % 2 != 0:
        got.append(string[-1])

    return ''.join(got)

