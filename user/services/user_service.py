from user.repositories import UserRepository
from user.models import User


class UserService:
    user_repo = UserRepository()

    def get_user_by_username(self, username: str):
        try:
            return self.user_repo.get_user_by_username(username)
        except User.DoesNotExist:
            return None
