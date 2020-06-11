import pytest
from src.user import UpdateUser


@pytest.fixture
def user():
    return UpdateUser()


@pytest.fixture(scope='function')
def create_user(self, user):
    response = self.api.post(self.api.USERS_URL, json=user.json_user())

    assert response.status_code == 201

    response_data = response.json()
    user.id = response_data['id']
    print(f'--> user created, id:{user.id}')

    return user, response_data


@pytest.fixture(scope='function')
def update_user(user):
    user.generate_user()
    return user, user.json_user()
