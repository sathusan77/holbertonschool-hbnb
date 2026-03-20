from app.models.amenity import Amenity
from app import db
from typing import List

class AmenityRepository:
    def add(self, amenity: Amenity) -> Amenity:
        db.session.add(amenity)
        db.session.commit()
        return amenity

    def get_by_id(self, amenity_id: str) -> Amenity:
        return Amenity.query.get(amenity_id)

    def get_all(self) -> List[Amenity]:
        return Amenity.query.all()

    def update(self, amenity: Amenity) -> Amenity:
        db.session.commit()
        return amenity

    def delete(self, amenity: Amenity) -> bool:
        db.session.delete(amenity)
        db.session.commit()
        return True
