import pytest

from server.command import reversed_string 


@pytest.mark.asyncio
async def test_reversed_string():
    s = 'abcd'

    got = await reversed_string(s)

    assert got == ''.join(reversed(s))

