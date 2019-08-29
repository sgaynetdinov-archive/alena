import pytest

from server.queue import get_queue


@pytest.mark.asyncio
async def test_singelton():
    queue = get_queue()

    assert queue is get_queue()


@pytest.mark.asyncio
async def test_queue():
    queue = get_queue()
    item = 100500

    await queue.put(item)

    assert await queue.size() == 1
    assert await queue.pop() == item
    assert await queue.size() == 0

