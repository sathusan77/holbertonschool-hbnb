from flask import request, jsonify
from app.models.user import User
from app import db
from flask_jwt_extended import jwt_required

def create_user():
    data = request.get_json()

    # Vérifier password
    password = data.get("password")
    if not password:
        return jsonify({"error": "Password required"}), 400

    user = User(
        email=data.get("email"),
        first_name=data.get("first_name"),
        last_name=data.get("last_name")
    )

    # 🔐 Hash ici
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201
