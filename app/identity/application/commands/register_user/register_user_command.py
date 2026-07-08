from app.identity.domain.value_objects.password import Password

class RegisterUserCommand:
    def __init__(self, email: str, password: Password):
        self.email = email
        self.password = password