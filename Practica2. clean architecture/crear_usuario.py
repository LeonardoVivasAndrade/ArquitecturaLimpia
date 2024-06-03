from usuario_repo import SqliteUsuarioRepo
from user import User

class CrearUsuario:
    def __init__(self, usuario_repo):
        self.usuario_repo = usuario_repo

    def ejecutar(self, nombre, correo, contrasena):        
        usuario = User(None, nombre, correo, contrasena)
        nuevo_id = self.usuario_repo.guardar(usuario)
        usuario.id = nuevo_id
        return usuario
    
    def buscar_por_correo(self, correo):        
        usuario = self.usuario_repo.obtener_por_correo(correo)
        return usuario