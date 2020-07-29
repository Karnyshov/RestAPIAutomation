from src.template import Template
import pytest


class TestSignUp(Template):

    def test_signup(self):
        response = self.api.post(self.api.REGISTER_URL, json={
            'email': 'eve.holt@reqres.in',
            'password': 'pistol'
        })

        assert 200 == response.status_code
        assert 4 == response.json()['id']
        assert "QpwL5tke4Pnpja7X4" == response.json()['token']

    @pytest.mark.xfail
    def test_signup_negative_password(self):
        response = self.api.post(self.api.REGISTER_URL, json={'email': 'eve.holt@reqres.in'})

        assert 400 == response.status_code
        assert "Missing password" == response.json()['error']

    @pytest.mark.xfail
    def test_signup_negative_email(self):
        response = self.api.post(self.api.REGISTER_URL, json={'password': 'pistol'})

        assert 400 == response.status_code
        assert "Missing email or username" == response.json()['error']
