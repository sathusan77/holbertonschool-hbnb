from app import db, bcrypt
import uuid


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = db.Column(db.String(128), nullable=False, unique=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))

    # 🔐 mot de passe hashé
    password = db.Column(db.String(128), nullable=False)

    # 🔑 hash du mot de passe
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    # 🔍 vérifier mot de passe
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    # 🚫 ne pas exposer password
    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
