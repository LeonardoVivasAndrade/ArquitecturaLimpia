import sqlite3
from user import User

class SqliteUsuarioRepo:
    def __init__(self):
        self.conexion = sqlite3.connect('usuarios.db')
        self.cursor = self.conexion.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS usuario (id INTEGER PRIMARY KEY, nombre TEXT, correo TEXT, contasena TEXT)')

    def guardar(self, usuario):
        self.cursor.execute('INSERT INTO usuario VALUES (?, ?, ?, ?)', (usuario.id, usuario.nombre, usuario.correo, usuario.contrasena))
        self.conexion.commit()
        return self.cursor.lastrowid

    def obtener_por_correo(self, correo):
        cursor = self.conexion.cursor()
        self.cursor.execute('SELECT * FROM usuario WHERE correo = ?', (correo,))
        fila = self.cursor.fetchone()
        if fila:
            return User(fila[0], fila[1], fila[2], fila[3])
        else:
            return None
