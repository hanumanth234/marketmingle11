from EAPP import db
from models.product_models import Product
from werkzeug.exceptions import NotFound

class ProductService:
    @staticmethod
    def create_product(seller_id, category_id, product_name, product_price, product_rating):
        new_product = Product(
            Seller_Id=seller_id,
            Category_Id=category_id,
            Product_Name=product_name,
            Product_Price=product_price,
            Product_Rating=product_rating
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product

    @staticmethod
    def get_product_by_id(product_id):
        # Fetching product along with the associated category and seller using relationships
        product = Product.query.filter_by(Product_Id=product_id).first()
        if not product:
            raise NotFound('Product not found')
        
        # Returning product details with related category and seller information
        return {
            'Product_Id': product.Product_Id,
            'Seller_Id': product.Seller_Id,
            'Seller_Fullname': product.seller.User_Fullname,  # Assuming 'User_Name' is a field in Users table
            'Category_Id': product.Category_Id,
            'Category_Name': product.category.Category_Name,  # Assuming 'Category_Name' is a field in Categories table
            'Product_Name': product.Product_Name,
            'Product_Price': product.Product_Price,
            'Product_Rating': product.Product_Rating
        }

    @staticmethod
    def get_all_products():
        products = Product.query.all()
        return [{
            'Product_Id': product.Product_Id,
            'Seller_Id': product.Seller_Id,
            'Seller_Fullname': product.seller.User_Fullname,  # Assuming 'User_Name' is a field in Users table
            'Category_Id': product.Category_Id,
            'Category_Name': product.category.Category_Name,  # Assuming 'Category_Name' is a field in Categories table
            'Product_Name': product.Product_Name,
            'Product_Price': product.Product_Price,
            'Product_Rating': product.Product_Rating
        } for product in products]

    @staticmethod
    def update_product(product_id, seller_id, category_id, product_name, product_price, product_rating):
        product = Product.query.get(product_id)
        if not product:
            raise NotFound('Product not found')

        product.Seller_Id = seller_id
        product.Category_Id = category_id
        product.Product_Name = product_name
        product.Product_Price = product_price
        product.Product_Rating = product_rating

        db.session.commit()
        return product

    @staticmethod
    def delete_product(product_id):
        product = Product.query.get(product_id)
        if not product:
            raise NotFound('Product not found')
        
        db.session.delete(product)
        db.session.commit()
        return {'message': 'Product deleted successfully'}
    
