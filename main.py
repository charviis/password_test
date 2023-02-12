import random
import string

class Password:
    def __init__(self, password):
        self.password = password

    def generate(self, length=8, complexity="normal"):
        """
        Generates a password with specified length and complexity.
        """
        if complexity == "weak":
            self.password = ''.join(random.choices(string.ascii_lowercase, k=length))
        elif complexity == "normal":
            self.password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        elif complexity == "strong":
            self.password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        else:
            raise ValueError("Invalid complexity level")

    def check(self, password2):
        """
        Checks if two passwords are equal.
        """
        return self.password == password2

class PasswordTest:
    def test_generate(self):
        password = Password("")
        password.generate()
        assert len(password.password) == 8
        password.generate(length=16)
        assert len(password.password) == 16
        password.generate(complexity="weak")
        assert all(c in string.ascii_lowercase for c in password.password)
        password.generate(complexity="normal")
        assert all(c in (string.ascii_letters + string.digits) for c in password.password)
        password.generate(complexity="strong")
        assert all(c in (string.ascii_letters + string.digits + string.punctuation) for c in password.password)

        try:
            password.generate(complexity="invalid")
        except ValueError as ve:
            assert str(ve) == "Invalid complexity level"

    def test_check(self):
        password = Password("password")
        assert password.check("password")
        assert not password.check("Password")
