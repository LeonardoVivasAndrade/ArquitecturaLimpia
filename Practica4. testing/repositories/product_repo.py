import sqlite3
from entities.product import Product

class SqliteProductRepo:
    def __init__(self):
        self.conexion = sqlite3.connect('ventas.db')
        self.cursor = self.conexion.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS product (id INTEGER PRIMARY KEY, description TEXT, price NUMERIC)')

    def guardar(self, product):
        self.cursor.execute('INSERT INTO product VALUES (?, ?, ?)', (product.id, product.description, product.price))
        self.conexion.commit()
        return self.cursor.lastrowid
