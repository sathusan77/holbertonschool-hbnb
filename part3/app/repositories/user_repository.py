from app.models.user import User
from app import db
from typing import List

class UserRepository:
    """Repository spécifique pour les Users"""

    # CREATE
    def add(self, user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user

    # READ
    def get_by_id(self, user_id: str) -> User:
        return User.query.get(user_id)

    def get_by_email(self, email: str) -> User:
        return User.query.filter_by(email=email).first()

    def get_all(self) -> List[User]:
        return User.query.all()

    # UPDATE
    def update(self, user: User) -> User:
        db.session.commit()
        return user

    # DELETE
    def delete(self, user: User) -> bool:
        db.session.delete(user)
        db.session.commit()
        return True
