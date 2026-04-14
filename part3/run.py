# run.py
from app import create_app
from flask_jwt_extended import JWTManager
from app.models import db  # assuming your SQLAlchemy instance is in app/models/__init__.py or similar

# Crée l'application avec la config de développement
app = create_app('config.DevelopmentConfig')

# Initialise JWT avec l'application
jwt = JWTManager(app)

# Initialise la DB avec l'application
db.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
