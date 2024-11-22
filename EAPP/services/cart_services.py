from EAPP import db
from models.cart_models import Cart
from werkzeug.exceptions import NotFound

class CartService:
    @staticmethod
    def add_to_cart(product_id, user_id, cart_size, product_quantity, cart_amount):
        new_cart = Cart(
            Product_Id=product_id,
            User_Id=user_id,
            Cart_Size=cart_size,
            Product_Quantity=product_quantity,
            Cart_Amount=cart_amount
        )
        db.session.add(new_cart)
        db.session.commit()
        return new_cart

    @staticmethod
    def get_cart_by_id(cart_id):
        cart = Cart.query.get(cart_id)
        if not cart:
            raise NotFound('Cart item not found')
        return cart

    @staticmethod
    def get_all_carts():
        return Cart.query.all()

    @staticmethod
    def update_cart(cart_id, cart_size=None, product_quantity=None, cart_amount=None):
        cart = Cart.query.get(cart_id)
        if not cart:
            raise NotFound('Cart item not found')
        
        cart.Cart_Size = cart_size if cart_size is not None else cart.Cart_Size
        cart.Product_Quantity = product_quantity if product_quantity is not None else cart.Product_Quantity
        cart.Cart_Amount = cart_amount if cart_amount is not None else cart.Cart_Amount
        
        db.session.commit()
        return cart

    @staticmethod
    def delete_cart(cart_id):
        cart = Cart.query.get(cart_id)
        if not cart:
            raise NotFound('Cart item not found')
        
        db.session.delete(cart)
        db.session.commit()
        return {'message': 'Cart item deleted successfully'}