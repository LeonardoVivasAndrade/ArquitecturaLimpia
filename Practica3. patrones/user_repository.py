from user_entity import UserEntity

class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_user(self, user_id):    
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        result = cursor.fetchone()
        return UserEntity(result[0], result[1], result[2])