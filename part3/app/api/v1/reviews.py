from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.review import Review
from app.models.place import Place
from app import db

reviews_bp = Blueprint("reviews", __name__, url_prefix="/api/v1/reviews")


@reviews_bp.route("/", methods=["POST"])
@jwt_required()
def create_review():
    data = request.get_json()
    user_id = get_jwt_identity()

    place = Place.query.get(data.get("place_id"))

    if not place:
        return {"error": "Place not found"}, 404

    # ❌ interdit de review son propre place
    if place.user_id == user_id:
        return {"error": "You cannot review your own place"}, 400

    # ❌ interdit doublon
    existing = Review.query.filter_by(
        user_id=user_id,
        place_id=place.id
    ).first()

    if existing:
        return {"error": "Already reviewed"}, 400

    review = Review(
        text=data.get("text"),
        user_id=user_id,
        place_id=place.id
    )

    db.session.add(review)
    db.session.commit()

    return jsonify(review.to_dict()), 201
