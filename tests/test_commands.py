import pytest

from server import is_valid_command, status_task, get_cache

@pytest.mark.asyncio
@pytest.mark.parametrize("command_name,expected",[
    ("create_task", True),
    ("status_task", True),
    ("result_task", True),
    ("all_task", False),
    ("remove_task", False),
])
async def test_is_valid_command(command_name, expected):
    assert await is_valid_command(command_name) == expected


@pytest.mark.asyncio
async def test_status_task__task_uuid_not_found():
    got = await status_task('100500') 
    assert got == "не найдено"


@pytest.mark.asyncio
async def test_status_task():
    cache = get_cache()
    task_uuid = await cache.add('100500')

    assert '100500' == await status_task(task_uuid)
