from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models.user import User

auth_bp = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing data"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    # chercher user
    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    # 🔐 créer token
    access_token = create_access_token(identity=user.id)

    return jsonify({
        "access_token": access_token
    }), 200
