import random
import string


class Generator:
    @staticmethod
    def generate_random_string(n):
        return ''.join([random.choice(string.ascii_letters + string.digits) for x in range(n)])

    @staticmethod
    def generate_email(n):
        return ''.join([random.choice(string.ascii_letters + string.digits) for x in range(n)])\
               + '@.com'
