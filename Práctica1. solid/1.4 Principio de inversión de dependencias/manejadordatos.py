from basedatos import BaseDatos

class ManejadorDatos:
    def procesar(self, base_datos):
        base_datos.guardar("Datos de prueba")
        datos_leidos = base_datos.leer()
        print("Datos leídos = ", datos_leidos)