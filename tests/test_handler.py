import pytest

from server.cache import get_cache
from server.task import Task
from server.status import Status
from server.handler import handler, status_task, result_task, create_task
from server.queue import get_queue


@pytest.mark.asyncio
@pytest.mark.parametrize("handler_name,expected",[
    ("all_task", "неверная команда"),
    ("remove_task", "неверная команда"),
])
async def test_is_not_valid_handler(handler_name, expected):
    assert await handler(handler_name) == expected


@pytest.mark.asyncio
async def test_status_task__task_uuid_not_found():
    got = await handler(f"status_task 100500") 
    assert got == "не найдено"


@pytest.mark.asyncio
async def test_status_task():
    task = Task('reversed string', Status.QUEUE.value)
    cache = get_cache()
    task_uuid = await cache.add('100500', task.as_json())

    assert Status.QUEUE.value == await handler(f"status_task {task_uuid}")


@pytest.mark.asyncio
async def test_result_task__task_uuid_not_found():
    got = await handler(f"result_task 100500")
    assert got == "не найдено" 


@pytest.mark.asyncio
@pytest.mark.parametrize("status, expected", [
    (Status.QUEUE.value, "не найдено"),
    (Status.IN_PROGRESS.value, "не найдено"),
    (Status.COMPLETED.value, "100500"),
])
async def test_result_task__check_status(status, expected):
    task = Task('string', status, expected)
    cache = get_cache()
    task_uuid = await cache.add('100500', task.as_json())

    got = await handler(f"result_task {task_uuid}")

    assert got == expected


@pytest.mark.asyncio
async def test_create_task():
    cache = get_cache()
    queue = get_queue()

    assert await queue.size() == 0

    task_uuid = await handler(f"create_task reversed_string abcd")
    task = Task.from_json(await cache.get(task_uuid))

    assert task.command == "reversed_string abcd"
    assert task.status == Status.QUEUE.value
    assert task.uuid == task_uuid
    assert await queue.size() == 1
    await queue.pop()

@pytest.mark.asyncio
async def test_create_invalid_command():
    got = await handler(f"create_task not_command")

    assert got == "неверная команда"

