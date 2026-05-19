from app.identity.domain.entities.users import User
from app.identity.infrastructure.persistence.sqlalchemy.models.user_model import UserModel

class UserMapper:
    @staticmethod
    def to_entity(user_model: UserModel) -> User:
        return User(
            id=user_model.id,
            email=user_model.email,
            hashed_password=user_model.hashed_password,
        )

    @staticmethod
    def to_model(user: User) -> UserModel:
        return UserModel(
            id=user.id,
            email=user.email,
            hashed_password=user.hashed_password,
        )