from flask import Blueprint, jsonify, abort
from app.models.data import users

users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


@users_bp.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    return jsonify(user)
