from repositories.product_repo import SqliteProductRepo
from entities.cart import Cart


class CartManager():
    def __init__(self, Cart):
        self.cart = Cart

    def add(self, product, quantity):
        if product.price >= 0:
            item = {"id":product.id, "quantity": quantity}
            self.cart.listProducts.append(item)
            if product.price > 100:
                dcto = product.price * 0.1
                self.cart.total += (product.price - dcto)
            else:
                self.cart.total += product.price    
            return self.cart.listProducts        
        else:
            None