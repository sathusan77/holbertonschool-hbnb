from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.place import Place
from app import db

places_bp = Blueprint("places", __name__, url_prefix="/api/v1/places")


@places_bp.route("/", methods=["POST"])
@jwt_required()
def create_place():
    data = request.get_json()
    user_id = get_jwt_identity()

    place = Place(
        name=data.get("name"),
        user_id=user_id  # 🔥 important
    )

    db.session.add(place)
    db.session.commit()

    return jsonify(place.to_dict()), 201
