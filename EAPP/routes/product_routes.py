from flask import Blueprint, request, jsonify , url_for, render_template
from ..controllers.product_controllers import ProductController
from ..models.product_models import Product  # Make sure this import is correct
from ..models.category_models import Category  # Import the Category model

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()

    # Check if category exists
    category_id = data.get('Category_Id')
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404

    return ProductController.create_product()

@product_bp.route('/api/products', methods=['GET'])
def get_all_products():
    return ProductController.get_all_products()

@product_bp.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return ProductController.get_product(product_id)

@product_bp.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()

    # Check if category exists before updating
    category_id = data.get('Category_Id')
    if category_id:
        category = Category.query.get(category_id)
        if not category:
            return jsonify({'error': 'Category not found'}), 404

    return ProductController.update_product(product_id)

@product_bp.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    return ProductController.delete_product(product_id)

# New Route: Get products by category
@product_bp.route('/api/products/category/<int:category_id>', methods=['GET'])
def get_products_by_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404

    products = Product.query.filter_by(Category_Id=category_id).all()
    if not products:
        return jsonify({'message': 'No products found in this category'}), 404

    return jsonify([{
        'Product_Id': product.Product_Id,
        'Seller_Id': product.Seller_Id,
        'Product_Name': product.Product_Name,
        'Product_Price': product.Product_Price,
        'Product_Rating': product.Product_Rating,
        'Category_Id': product.Category_Id
    } for product in products]), 200

@product_bp.route('/api/products/category_id', methods=['GET'])
def get_category_id_by_name():
    category_name = request.args.get('category_name')
    if not category_name:
        return jsonify({'error': 'Category name is required'}), 400
    
    # Fetch category by name
    category = Category.query.filter_by(Category_Name=category_name).first()
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    
    return jsonify({'Category_Id': category.Category_Id}), 200

@product_bp.route('/products/category/<int:category_id>')
def products_by_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return "Category not found", 404

    products = Product.query.filter_by(Category_Id=category_id).all()
    return render_template('products.html', 
                           category_name=category.Category_Name, 
                           products=[{
                               'Product_Name': product.Product_Name,
                               'Product_Price': product.Product_Price,
                               'Product_Rating': product.Product_Rating,
                               'image_url': url_for('static', filename=f'images/{product.Product_Id}.jpg')
                           } for product in products])