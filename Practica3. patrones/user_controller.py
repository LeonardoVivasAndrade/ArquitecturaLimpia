class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    def get_user(self, user_id):
        user = self.user_service.get_user(user_id)    
        return f"Name: {user.name}, Email: {user.email}"
