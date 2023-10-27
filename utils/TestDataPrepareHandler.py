import random
import string


class TestDataHelperHandler:

    @staticmethod
    def generate_email():
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
        domain = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        extension = random.choice(['com', 'net', 'org', 'io'])

        email = f"{username}@{domain}.{extension}"
        return email

    @staticmethod
    def generate_password():
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return password
