from flask import request, jsonify
from ..models.cart_models import Cart
from EAPP import db

class CartController:
    @staticmethod
    def get_all_carts():
        carts = Cart.query.all()
        return jsonify([{
            'Cart_Id': cart.Cart_Id,
            'Product_Id': cart.Product_Id,
            'User_Id': cart.User_Id,
            'Cart_Size': cart.Cart_Size,
            'Product_Quantity': cart.Product_Quantity,
            'Cart_Amount': cart.Cart_Amount
        } for cart in carts]), 200

    @staticmethod
    def get_cart(cart_id):
        cart = Cart.query.get(cart_id)
        if not cart:
            return jsonify({'error': 'Cart not found'}), 404
        return jsonify({
            'Cart_Id': cart.Cart_Id,
            'Product_Id': cart.Product_Id,
            'User_Id': cart.User_Id,
            'Cart_Size': cart.Cart_Size,
            'Product_Quantity': cart.Product_Quantity,
            'Cart_Amount': cart.Cart_Amount
        }), 200

    @staticmethod
    def add_to_cart():
        data = request.get_json()
        product_id = data.get('Product_Id')
        user_id = data.get('User_Id')
        cart_size = data.get('Cart_Size')
        product_quantity = data.get('Product_Quantity')
        cart_amount = data.get('Cart_Amount')

        new_cart = Cart(
            Product_Id=product_id,
            User_Id=user_id,
            Cart_Size=cart_size,
            Product_Quantity=product_quantity,
            Cart_Amount=cart_amount
        )
        
        db.session.add(new_cart)
        db.session.commit()
        return jsonify({'message': 'Added to cart successfully', 'Cart_Id': new_cart.Cart_Id}), 201

    @staticmethod
    def update_cart(cart_id):
        data = request.get_json()
        cart = Cart.query.get(cart_id)
        if not cart:
            return jsonify({'error': 'Cart not found'}), 404

        cart.Cart_Size = data.get('Cart_Size', cart.Cart_Size)
        cart.Product_Quantity = data.get('Product_Quantity', cart.Product_Quantity)
        cart.Cart_Amount = data.get('Cart_Amount', cart.Cart_Amount)

        db.session.commit()
        return jsonify({'message': 'Cart updated successfully'}), 200

    @staticmethod
    def delete_cart(cart_id):
        cart = Cart.query.get(cart_id)
        if not cart:
            return jsonify({'error': 'Cart not found'}), 404

        db.session.delete(cart)
        db.session.commit()
        return jsonify({'message': 'Cart deleted successfully'}), 200