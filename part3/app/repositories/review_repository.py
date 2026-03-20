from app.models.review import Review
from app import db
from typing import List

class ReviewRepository:
    def add(self, review: Review) -> Review:
        db.session.add(review)
        db.session.commit()
        return review

    def get_by_id(self, review_id: str) -> Review:
        return Review.query.get(review_id)

    def get_all(self) -> List[Review]:
        return Review.query.all()

    def update(self, review: Review) -> Review:
        db.session.commit()
        return review

    def delete(self, review: Review) -> bool:
        db.session.delete(review)
        db.session.commit()
        return True
