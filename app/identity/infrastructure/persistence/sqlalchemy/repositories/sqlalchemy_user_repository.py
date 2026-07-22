from sqlalchemy.orm import Session

from app.identity.domain.entities.user import User
from app.identity.domain.repositories.user_repository_interface import UserRepositoryInterface
from app.identity.domain.value_objects.user_id import UserId
from app.identity.infrastructure.persistence.sqlalchemy.models.user_model import UserModel
from app.identity.infrastructure.persistence.sqlalchemy.mappers.user_mapper import UserMapper

class SQLAlchemyUserRepository(UserRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def find(self, id: UserId) -> User | None:
        user_model = self.db.query(UserModel).filter(UserModel.id == id).first()
        
        if user_model:
            return UserMapper.to_entity(user_model)
        return None
    
    def find_by_email(self, email: str) -> User | None:
        user_model = self.db.query(UserModel).filter(UserModel.email == email).first()
        if user_model:
            return UserMapper.to_entity(user_model)
        return None

    def save(self, user) -> User:
        user_model = UserMapper.to_model(user)
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return UserMapper.to_entity(user_model)