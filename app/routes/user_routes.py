from app.middlewares import UserMiddleware
from flask import Blueprint, request
from app.controllers import UserController

user_bp = Blueprint("users", __name__)
verify_email = UserMiddleware.verify_user_email
validate_email = UserMiddleware.validate_user_email
check_password = UserMiddleware.check_user_password


@user_bp.route("/signup", methods=["POST"])
@verify_email
def user_signup():
    try:
        data = request.get_json()
        email = data["email"]
        first_name = data["firstname"]
        last_name = data["lastname"]
        password = data["password"]
        user = UserController.user_signup(first_name, last_name, email, password)
        return {"message": "User created successfully", "data": user}, 201
    except Exception as e:
        return {"message": e, "data": user}, 400


@user_bp.route("/login", methods=["POST"])
@validate_email
@check_password
def user_login():
    try:
        data = request.get_json()
        email = data["email"]

        user = UserController.user_login(email)
        if user:
            return {"message": "User logged in successfully", "data": user}, 200
        else:
            return {"message": "Error while processing, it's not you it's us"}, 500
    except Exception as e:
        return {"message": e}, 400
