from pymongo import MongoClient
from basedatos import BaseDatos

class MongoDB(BaseDatos):
    def guardar(self, datos):
        client = MongoClient("localhost", 27017)        
        db = client.test_database
        posts = db.posts        
        post_id = posts.insert_one(datos).inserted_id        
        
    def leer(self):
        client = MongoClient("localhost", 27017)
        db = client.test_database
        posts = db.posts        
        result = posts.find()
        return result