import mysql.connector
from basedatos import BaseDatos

class MySQL(BaseDatos):
    def guardar(self, datos):
        cnx = mysql.connector.connect(host = "localhost", user = "Username", password = "Password", database = "solid")
        cursor = cnx.cursor()
        query = ("INSERT INTO datos (dato) VALUES (%s)")
        cursor.execute(query, datos)
        cnx.commit()
        cursor.close()
        cnx.close()
        
    def leer(self):
        cnx = mysql.connector.connect(host = "localhost", user = "Username", password = "Password", database = "solid")
        cursor = cnx.cursor()
        cursor.excute("SELECT * FROM datos")
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result
        
        