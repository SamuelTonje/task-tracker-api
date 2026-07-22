from app.identity.application.queries.get_user.get_user_query import GetUserQuery
from app.identity.application.queries.get_user.get_user_result import GetUserResult
from app.identity.domain.repositories.user_repository_interface import UserRepositoryInterface

class GetUserHandler:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository
        pass

    def handle(self, user_query: GetUserQuery) -> GetUserResult:
        existing_user = self.user_repository.find(user_query.id)
        if not existing_user:
            raise Exception("User not found")
        
        return GetUserResult(existing_user.id, existing_user.email)