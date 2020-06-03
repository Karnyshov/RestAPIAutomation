from src.data_generator import Generator
import json


class User:
    def __init__(self, name=None, job=None, user_id=None, email=None, password=None):
        self.name = name
        self.job = job
        self.user_id = user_id
        self.email = email
        self.password = password

    def get_name(self):
        return self.name

    def get_job(self):
        return self.job

    def get_user_id(self):
        return self.user_id

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def set_name(self, name):
        self.name = name

    def set_job(self, job):
        self.job = job

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def generate_user_data(self):
        self.set_name(Generator.generate_random_string(5))
        self.set_email(Generator.generate_email(5))
        self.set_password(Generator.generate_random_string(9))
        self.set_job(Generator.generate_random_string(6))

    def generate_credentials(self):
        self.set_email(Generator.generate_email(5))
        self.set_password(Generator.generate_random_string(9))

    def generate_user(self):
        self.set_name(Generator.generate_random_string(5))
        self.set_job(Generator.generate_email(5))

    def json_credentials(self):
        return json.dumps({
            "email": self.email,
            "password": self.password
        })

    def json_user(self):
        return json.dumps({
            "name": self.name,
            "jon": self.job
        })

    def json_user_data(self):
        return json.dumps({
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "job": self.job
        })


class FullUser(User):
    def __init__(self):
        super().__init__()
        self.generate_user_data()


class SignUpUser(User):
    def __init__(self):
        super().__init__()
        self.generate_credentials()


# Used for User create/update
class UpdateUser(User):
    def __init__(self):
        super().__init__()
        self.generate_user()
