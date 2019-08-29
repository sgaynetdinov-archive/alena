import pytest

from server import get_cache, Task, Status
from server.handler import handler, status_task, result_task, create_task

@pytest.mark.asyncio
@pytest.mark.parametrize("handler_name,expected",[
    ("all_task", "неверная команда"),
    ("remove_task", "неверная команда"),
])
async def test_is_not_valid_handler(handler_name, expected):
    assert await handler(handler_name) == expected


@pytest.mark.asyncio
async def test_status_task__task_uuid_not_found():
    got = await handler("status_task", "100500") 
    assert got == "не найдено"


@pytest.mark.asyncio
async def test_status_task():
    task = Task('reversed string', Status.QUEUE)
    cache = get_cache()
    task_uuid = await cache.add(task.as_dict())

    assert Status.QUEUE == await handler("status_task", task_uuid)


@pytest.mark.asyncio
async def test_result_task__task_uuid_not_found():
    got = await handler("result_task", "100500")
    assert got == "не найдено" 


@pytest.mark.asyncio
@pytest.mark.parametrize("status, expected", [
    (Status.QUEUE, "не найдено"),
    (Status.IN_PROGRESS, "не найдено"),
    (Status.COMPLETED, "100500"),
])
async def test_result_task__check_status(status, expected):
    task = Task('string', status, expected)
    cache = get_cache()
    task_uuid = await cache.add(task.as_dict())

    got = await handler("result_task", task_uuid)

    assert got == expected


@pytest.mark.asyncio
async def test_create_task():
    cache = get_cache()

    task_uuid = await handler("create_task", "reversed_string")

    task = await cache.get(task_uuid)
    assert task['command'] == "reversed_string"
