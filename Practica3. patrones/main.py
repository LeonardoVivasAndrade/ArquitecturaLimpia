import mysql.connector

from mysql_user_repository import MySQLUserRepository

if __name__ == "__main__":
    conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='Curso'
        )
    conexion.cursor().execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255))")
    
    user_repo = MySQLUserRepository(conexion)
    usuario = user_repo.get_user(1)
    if usuario == None:
        print("No se encontro")
    else:
        print(usuario.name)