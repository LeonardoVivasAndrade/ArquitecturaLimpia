from pytest_bdd import scenario, given, when, then
from entities.product import Product
from use_cases.cart_manager import CartManager
from entities.cart import Cart

@scenario('test_cart.feature', 'Add product with price greater than $100')
def test_add_product_with_price_greater_than_100():
    pass

@given('a shopping cart with no products')
def empty_cart():    
    return CartManager(Cart())

@when('I add a product with price $150')
def add_expensive_product(empty_cart):
    product = Product(1, "Product mayor a 100", 150)
    empty_cart.add(product, 1)

@then('the cart total should be $135')
def check_cart_total(empty_cart):
    assert empty_cart.cart.total == 135