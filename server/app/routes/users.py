from flask import Blueprint, jsonify, request
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


@users_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data or "age" not in data:
        return jsonify({"message": "Missing data"}), 404
    new_id = str(max(map(int, users.keys())) + 1)
    new_user = {"name": data["name"], "email": data["email"], "age": data["age"]}
    users[new_id] = new_user
    return jsonify({"id": new_id, "user": new_user}), 201
