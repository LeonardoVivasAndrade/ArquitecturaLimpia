from flask import Flask, request, jsonify
from repositories.product_repo import SqliteProductRepo
from use_cases.create_product import CreateProduct
from use_cases.cart_manager import CartManager
from entities.cart import Cart

app = Flask(__name__)

@app.route('/productos', methods=['POST'])
def crear_producto():
    description = request.form['description']
    price = request.form['price']

    use_case_create_product = CreateProduct(SqliteProductRepo())
    product = use_case_create_product.ejecutar(description, price)

    use_case_add_to_cart = CartManager(Cart())
    use_case_add_to_cart.add(product, 1)
    use_case_add_to_cart.add(product, 5)
    #use_case_add_to_cart.get_list()



    return jsonify({'id': product.id, 'description': product.description, 'price': product.price})


