import uuid

from app.identity.domain.entities.user import User
from app.identity.domain.repositories.user_repository_interface import UserRepositoryInterface
from app.identity.domain.services.password_hasher_interface import PasswordHasherInterface
from app.identity.domain.value_objects.user_id import UserId
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
    
        hashed_password = self.password_hasher.hash(command.password.value)
        new_user = self.user_repository.save(
            User(id=UserId(str(uuid.uuid4())).value, email=command.email, hashed_password=hashed_password)
        )

        return RegisterUserResult(id=new_user.id, email=new_user.email)
