import pytest

from server.command import reversed_string, transposition


@pytest.mark.asyncio
async def test_reversed_string():
    s = 'abcd'

    got = await reversed_string(s)

    assert got == ''.join(reversed(s))


@pytest.mark.asyncio
@pytest.mark.parametrize('string,expected', [
    ('abcd', 'badc'),
    ('abcde', 'badce'),
])
async def test_transposition(string, expected):
    got = await transposition(string)

    assert got == expected 

