class MySQLUserRepository:
    def __init__(self, db):
        self.db = db
    
    def get_user(self, user_id):    
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        result = cursor.fetchone()
        return {'name': result[1], 'email': result[2]}
