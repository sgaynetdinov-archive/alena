import pytest

from server import is_valid_command 

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

