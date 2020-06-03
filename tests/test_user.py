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

    def test_create_user(self, user_id):
        response = self.api.post(self.api.USERS_URL, user_id)

        assert 201 == response.status_code

    def test_update_user(self):
        response = self.api.post(self.api.USERS_URL, UpdateUser().json_user())

        assert 201 == response.status_code

    def test_patch_user(self):
        response = self.api.post(self.api.USERS_URL, UpdateUser().json_user())

        assert 201 == response.status_code

    def delete_user(self):
        response = self.api.delete(self.api.USERS_URL + "/2")

        assert 204 == response.status_code
