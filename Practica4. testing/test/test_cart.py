import pytest

from use_cases.cart_manager import CartManager
from entities.cart import Cart
from entities.product import Product

def test_add_product_to_cart():
    product = Product(1,"Product test",5000)
    cart = Cart()
    cart_manager = CartManager(cart)
    
    assert cart_manager.add(product, 1).len() != 0
    assert cart_manager.cart.total == 5000

def test_add_product_with_negative_price():    
    product = Product(2, "Product test negative price", -28000)
    cart = Cart()
    cart_manager = CartManager(cart)
    
    with pytest.raises(ValueError):
        cart_manager.add(product, 1).len()        