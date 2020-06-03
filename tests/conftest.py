import pytest
from src.user import UpdateUser


@pytest.fixture
def user():
    return UpdateUser()
