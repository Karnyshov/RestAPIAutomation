from src.template import Template
import pytest


class TestLogin(Template):

    def test_login(self):
        response = self.api.post(self.api.LOGIN_URL, json={
            'email': 'eve.holt@reqres.in',
            'password': 'cityslicka'
        })

        assert 200 == response.status_code
        assert "QpwL5tke4Pnpja7X4" == response.json()['token']

    @pytest.mark.xfail
    def test_login_negative_password(self):
        response = self.api.post(self.api.LOGIN_URL, json={'email': 'eve.holt@reqres.in'})

        assert 400 == response.status_code
        assert "Missing password" == response.json()['error']

    @pytest.mark.xfail
    def test_login_negative_email(self):
        response = self.api.post(self.api.LOGIN_URL, json={'password': 'cityslicka'})

        assert 400 == response.status_code
        assert "Missing email or username" == response.json()['error']

    @pytest.mark.xfail
    def test_login_no_user(self):
        response = self.api.post(self.api.LOGIN_URL, json={
            'email': 'test',
            'password': '123'
        })

        assert 400 == response.status_code
        assert "user not found" == response.json()['error']
