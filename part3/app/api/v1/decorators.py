from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import jsonify
from app.models.user import User

def admin_required(fn):
    """
    Décorateur pour protéger une route et autoriser uniquement les admins.
    Usage :
        @jwt_required()
        @admin_required
        def ma_route():
            ...
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # Récupère l'utilisateur connecté depuis le token
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        # Vérifie que c'est un admin
        if not user or not user.is_admin:
            return jsonify({"error": "Admin access required"}), 403

        # Si tout va bien, exécute la fonction
        return fn(*args, **kwargs)

    return wrapper
