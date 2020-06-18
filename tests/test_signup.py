from src.template import Template
import pytest


class TestSignUp(Template):

    def test_signup(self):
        pass

    @pytest.mark.xfail
    def test_signup_negative_password(self):
        pass

    @pytest.mark.xfail
    def test_signup_negative_email(self):
        pass
