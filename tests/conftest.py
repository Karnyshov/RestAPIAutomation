import pytest
from src.api import Api
from src.user import UpdateUser


@pytest.fixture()
def user_id():
    created_user = UpdateUser()
    created_user.json_user()
#    yield
#    created_user.user_id

#    print(created_user.user_id)
