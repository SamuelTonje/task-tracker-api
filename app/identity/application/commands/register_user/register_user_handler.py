import uuid

from app.identity.domain.entities.users import User
from app.identity.domain.repositories.user_repository_interface import UserRepositoryInterface
from app.identity.domain.services.password_hasher_interface import PasswordHasherInterface
from .register_user_command import RegisterUserCommand
from .register_user_result import RegisterUserResult

class RegisterUserHandler:
    def __init__(
        self,
        user_repository: UserRepositoryInterface,
        password_hasher: PasswordHasherInterface,
    ):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    def handle(self, command: RegisterUserCommand) -> RegisterUserResult:
        existing_user = self.user_repository.find_by_email(command.email)
        if existing_user:
            raise Exception("Email already in use")

        hashed_password = self.password_hasher.hash(command.password)
        new_user = self.user_repository.save(
            User(id=uuid.uuid4(), email=command.email, hashed_password=hashed_password)
        )

        return RegisterUserResult(id=new_user.id, email=new_user.email)
