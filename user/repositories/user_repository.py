from user.models import User


class UserRepository:
    def get_user_by_username(self, username: str):
        return User.objects.get(username=username)
