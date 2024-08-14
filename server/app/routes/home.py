from flask import Blueprint

home_bp = Blueprint("home", __name__)


@home_bp.route("/", methods=["GET"])
def home_check():
    return "Hello from flask server"