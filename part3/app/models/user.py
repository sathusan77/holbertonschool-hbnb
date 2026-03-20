from app import db, bcrypt
from app.models.base_model import BaseModel
from app.models.place import Place
from app.models.review import Review

class User(BaseModel):
    __tablename__ = "users"

    email = db.Column(db.String(128), nullable=False, unique=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    # ---------------- RELATIONS ----------------
    places = db.relationship("Place", backref="owner", lazy=True)
    reviews = db.relationship("Review", backref="author", lazy=True)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def to_dict(self, admin_view=False):
        data = {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
        if admin_view:
            data["is_admin"] = self.is_admin
        return data
