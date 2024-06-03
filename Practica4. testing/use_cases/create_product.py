from repositories.product_repo import SqliteProductRepo
from entities.product import Product

class CreateProduct:
    def __init__(self, product_repo):
        self.product_repo = product_repo

    def ejecutar(self, description, price):        
        product = Product(None, description, price)
        nuevo_id = self.product_repo.guardar(product)
        product.id = nuevo_id
        return product