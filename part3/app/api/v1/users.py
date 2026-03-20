from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app import db
from app.api.v1.decorators import admin_required
from app.repositories.user_repository import UserRepository

users_bp = Blueprint("users", __name__, url_prefix="/api/v1/users")
repo = UserRepository()  # <-- SQLAlchemy UserRepository

# ------------------ ROUTES PUBLIC ------------------

@users_bp.route("/", methods=["POST"])
def create_user():
    """
    Inscription d'un utilisateur normal
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data"}), 400

    email = data.get("email")
    if repo.get_by_email(email):
        return jsonify({"error": "Email already exists"}), 400

    password = data.get("password")
    if not password:
        return jsonify({"error": "Password required"}), 400

    user = User(
        email=email,
        first_name=data.get("first_name"),
        last_name=data.get("last_name")
    )
    user.set_password(password)

    repo.add(user)
    return jsonify(user.to_dict()), 201


# ------------------ ROUTES ADMIN ------------------

@users_bp.route("/admin", methods=["POST"])
@jwt_required()
@admin_required
def create_user_admin():
    """
    Créer un utilisateur (admin seulement)
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data"}), 400

    email = data.get("email")
    if repo.get_by_email(email):
        return jsonify({"error": "Email already exists"}), 400

    password = data.get("password")
    if not password:
        return jsonify({"error": "Password required"}), 400

    user = User(
        email=email,
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        is_admin=data.get("is_admin", False)
    )
    user.set_password(password)

    repo.add(user)
    return jsonify(user.to_dict(admin_view=True)), 201


@users_bp.route("/<user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    """
    Modifier son propre utilisateur
    """
    current_user_id = get_jwt_identity()
    if current_user_id != user_id:
        return {"error": "Unauthorized"}, 403

    user = repo.get_by_id(user_id)
    if not user:
        return {"error": "Not found"}, 404

    data = request.get_json()
    user.first_name = data.get("first_name", user.first_name)
    user.last_name = data.get("last_name", user.last_name)

    repo.update(user)
    return jsonify(user.to_dict()), 200


@users_bp.route("/admin/<user_id>", methods=["PUT"])
@jwt_required()
@admin_required
def update_user_admin(user_id):
    """
    Modifier n'importe quel utilisateur (admin)
    """
    user = repo.get_by_id(user_id)
    if not user:
        return {"error": "User not found"}, 404

    data = request.get_json()

    email = data.get("email")
    if email and email != user.email:
        if repo.get_by_email(email):
            return {"error": "Email already exists"}, 400
        user.email = email

    user.first_name = data.get("first_name", user.first_name)
    user.last_name = data.get("last_name", user.last_name)

    password = data.get("password")
    if password:
        user.set_password(password)

    if "is_admin" in data:
        user.is_admin = data["is_admin"]

    repo.update(user)
    return jsonify(user.to_dict(admin_view=True)), 200


@users_bp.route("/", methods=["GET"])
@jwt_required()
@admin_required
def get_all_users():
    """
    Récupérer tous les utilisateurs (admin seulement)
    """
    users = repo.get_all()
    return jsonify([u.to_dict(admin_view=True) for u in users])
