import requests


class Api:
    BASE_URL = "https://reqres.in/api/"
    RESOURCE_URL = BASE_URL + "unknown"
    USERS_URL = BASE_URL + "users"
    REGISTER_URL = BASE_URL + "register"
    LOGIN_URL = BASE_URL + "login"

    def __init__(self):
        self._headers = {"Content-Type": "application/json"}

    def get(self, url, params=None):
        return requests.get(url, params=params)

    def post(self, url, *args, **kwargs):
        return requests.post(url, *args, **kwargs)

    def put(self, url, data):
        return requests.put(url, data)

    def delete(self, url):
        return requests.delete(url)

    def patch(self, url, data):
        return requests.patch(url, data)
