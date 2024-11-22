from flask import Blueprint
from ..controllers.cart_controllers import CartController

cart_bp = Blueprint('cart_bp', __name__)

@cart_bp.route('/api/carts', methods=['POST'])
def add_to_cart():
    return CartController.add_to_cart()

@cart_bp.route('/api/carts', methods=['GET'])
def get_all_carts():
    return CartController.get_all_carts()

@cart_bp.route('/api/carts/<int:cart_id>', methods=['GET'])
def get_cart(cart_id):
    return CartController.get_cart(cart_id)

@cart_bp.route('/api/carts/<int:cart_id>', methods=['PUT'])
def update_cart(cart_id):
    return CartController.update_cart(cart_id)

@cart_bp.route('/api/carts/<int:cart_id>', methods=['DELETE'])
def delete_cart(cart_id):
    return CartController.delete_cart(cart_id)

