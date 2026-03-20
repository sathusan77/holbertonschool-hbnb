from app import db
from app.models.base_model import BaseModel
from app.models.review import Review
from app.models.amenity import Amenity
from app.models.association import place_amenity

class Place(BaseModel):
    __tablename__ = "places"

    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024))
    city = db.Column(db.String(128))
    state = db.Column(db.String(128))
    country = db.Column(db.String(128))
    price_by_night = db.Column(db.Float, default=0.0)
    number_rooms = db.Column(db.Integer, default=0)
    number_bathrooms = db.Column(db.Integer, default=0)
    max_guest = db.Column(db.Integer, default=0)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    user_id = db.Column(db.String(60), db.ForeignKey("users.id"), nullable=False)

    # ---------------- RELATIONS ----------------
    reviews = db.relationship("Review", backref="place", lazy=True)
    amenities = db.relationship(
        "Amenity",
        secondary=place_amenity,
        backref=db.backref("places", lazy=True)
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "price_by_night": self.price_by_night,
            "number_rooms": self.number_rooms,
            "number_bathrooms": self.number_bathrooms,
            "max_guest": self.max_guest,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "user_id": self.user_id
        }
