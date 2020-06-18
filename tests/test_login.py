from src.template import Template
import pytest


class TestLogin(Template):

    def test_login(self):
        pass

    @pytest.mark.xfail
    def test_login_negative_password(self):
        pass

    @pytest.mark.xfail
    def test_login_negative_email(self):
        pass
