from flask import Flask, request, jsonify
from usuario_repo import SqliteUsuarioRepo
from crear_usuario import CrearUsuario

app = Flask(__name__)

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    nombre = request.form['nombre']
    correo = request.form['correo']
    contrasena = request.form['contrasena']

    caso_de_uso = CrearUsuario(SqliteUsuarioRepo())
    usuario = caso_de_uso.ejecutar(nombre, correo, contrasena)
    usuario_busqueda = caso_de_uso.buscar_por_correo('leonardo@correo.com')
    print ("Usuario encontrado por correo id=", str(usuario_busqueda.id) + " nombre:" + usuario_busqueda.nombre)
    return jsonify({'id': usuario.id, 'nombre': usuario.nombre, 'correo': usuario.correo})
