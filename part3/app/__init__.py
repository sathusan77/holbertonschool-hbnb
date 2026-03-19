from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 🔐 JWT obligatoire
    app.config["JWT_SECRET_KEY"] = "super-secret-key"

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.api.v1.users import users_bp
    from app.api.v1.auth import auth_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(auth_bp)

    return app
