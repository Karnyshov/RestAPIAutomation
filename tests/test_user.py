import json

import pytest

from src.template import Template
from src.user import FullUser, UpdateUser, SignUpUser


class TestUser(Template):

    def test_single_user(self):
        response = self.api.get(self.api.USERS_URL)

        assert 200 == response.status_code

    def test_specific_user(self):
        response = self.api.get(self.api.USERS_URL + '/2')

        assert 200 == response.status_code
        assert 2 == response.json()['data']['id']
        assert 'janet.weaver@reqres.in' == response.json()['data']['email']
        assert 'Janet' == response.json()['data']['first_name']
        assert 'Weaver' == response.json()['data']['last_name']

    def test_user_absent(self):
        response = self.api.get(self.api.USERS_URL + "/0")

        assert 404 == response.status_code
        assert {} == response.json()

    def test_create_user(self, create_user):
        user, response = create_user

        assert user.name == response['name']
        assert user.job == response['job']

    def test_update_user(self, update_user):
        user, body = update_user

        response = self.api.put(self.api.USERS_URL + '{}'.format(user.id), json=body)

        assert 200 == response.status_code
        assert user.name == response.json()['name']
        assert user.job == response.json()['job']
        # print(f'--> user created, id:{user.id}')
        # user created and user_id received in test
        # add user update below

    def test_patch_user(self, create_user):
        pass
        # response = self.api.patch(self.api.USERS_URL, UpdateUser().json_user())

        # assert 201 == response.status_code

    def test_delete_user(self):
        response = self.api.delete(self.api.USERS_URL + "/2")

        assert 204 == response.status_code
