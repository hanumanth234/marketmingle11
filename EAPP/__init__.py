from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    from .routes.product_routes import product_bp
    app.register_blueprint(product_bp)

    from .routes.category_routes import category_bp
    app.register_blueprint(category_bp) 

    from .routes.cart_routes import cart_bp
    app.register_blueprint(cart_bp) 

    from .routes.order_routes import order_bp
    app.register_blueprint(order_bp) 

    from .routes.delivery_routes import delivery_bp
    app.register_blueprint(delivery_bp) 

    from .routes.payment_routes import payment_bp
    app.register_blueprint(payment_bp) 

    # Route to render index.html
    @app.route('/')
    def home():
        return render_template('snapshop.html')  

    @app.route('/register')
    def index():
        return render_template('register.html')

    @app.route('/categories')
    def categories():
        return render_template('categories.html')
    
    @app.route('/login')
    def login():
        return render_template('login.html')  
     
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)