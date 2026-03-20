from app.models.place import Place
from app import db
from typing import List

class PlaceRepository:
    def add(self, place: Place) -> Place:
        db.session.add(place)
        db.session.commit()
        return place

    def get_by_id(self, place_id: str) -> Place:
        return Place.query.get(place_id)

    def get_all(self) -> List[Place]:
        return Place.query.all()

    def update(self, place: Place) -> Place:
        db.session.commit()
        return place

    def delete(self, place: Place) -> bool:
        db.session.delete(place)
        db.session.commit()
        return True
