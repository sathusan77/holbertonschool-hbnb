from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# 🔧 Extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 🔐 JWT config
    app.config["JWT_SECRET_KEY"] = "super-secret-key"

    # 🔧 Init extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # 📦 Import blueprints
    from app.api.v1.users import users_bp
    from app.api.v1.auth import auth_bp
    from app.api.v1.places import places_bp
    from app.api.v1.reviews import reviews_bp

    # 🔗 Register blueprints
    app.register_blueprint(users_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(places_bp)
    app.register_blueprint(reviews_bp)

    return app
