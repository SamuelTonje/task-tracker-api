from app.identity.domain.repositories.user_repository_interface import UserRepositoryInterface
from app.identity.domain.services.password_hasher_interface import PasswordHasherInterface
from app.identity.domain.services.token_service_interface import TokenServiceInterface
from .login_user_command import LoginUserCommand
from .login_user_result import LoginUserResult

class LoginUserHandler:
    def __init__(
        self,
        user_repository: UserRepositoryInterface,
        password_hasher: PasswordHasherInterface,
        token_service: TokenServiceInterface,
    ):
        self.user_repository = user_repository
        self.password_hasher = password_hasher
        self.token_service = token_service

    def handle(self, command: LoginUserCommand) -> LoginUserResult:
        user = self.user_repository.find_by_email(command.email)
        if not user or not self.password_hasher.verify(command.password, user.hashed_password):
            raise Exception("Invalid email or password")

        token = self.token_service.create_access_token({"sub": user.email})
        
        return LoginUserResult(access_token=token)