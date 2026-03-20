from app import db
from app.models.user import User
from typing import List

class SQLAlchemyRepository:
    """
    Implémente la persistance avec SQLAlchemy.
    Fournit les méthodes CRUD pour les utilisateurs.
    """

    # ---------------- CREATE ----------------
    def add_user(self, user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user

    # ---------------- READ ----------------
    def get_user_by_id(self, user_id: str) -> User:
        return User.query.get(user_id)

    def get_user_by_email(self, email: str) -> User:
        return User.query.filter_by(email=email).first()

    def get_all_users(self) -> List[User]:
        return User.query.all()

    # ---------------- UPDATE ----------------
    def update_user(self, user: User) -> User:
        db.session.commit()
        return user

    # ---------------- DELETE ----------------
    def delete_user(self, user: User) -> bool:
        db.session.delete(user)
        db.session.commit()
        return True
