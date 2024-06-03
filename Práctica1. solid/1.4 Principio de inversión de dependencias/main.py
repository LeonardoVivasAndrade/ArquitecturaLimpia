from mysql import MySQL
from mongodb import MongoDB
from manejadordatos import ManejadorDatos

my_sql = MySQL()
mongo = MongoDB()

manejador_datos = ManejadorDatos()
manejador_datos.procesar(my_sql)
manejador_datos.procesar(mongo)