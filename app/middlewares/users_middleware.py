from app.services import AuthService
from flask import request, Response, g
from functools import wraps
from flask import current_app
from flask_bcrypt import Bcrypt


class UserMiddleware:

    @staticmethod
    def verify_user_email(func):
        @wraps(func)
        def verify_email(*args, **kwargs):
            reqq = request.get_json()
            email = reqq["email"]
            user = AuthService.find_user_by_email(email)

            if not user:
                return func(*args, **kwargs)

            return Response("User exists already", mimetype="text/plain", status=400)

        return verify_email

    @staticmethod
    def validate_user_email(func):
        @wraps(func)
        def validate_email(*args, **kwargs):
            reqq = request.get_json()
            email = reqq["email"]
            user = AuthService.find_user(email)

            if user:
                g.user = user
                return func(*args, **kwargs)
            return Response("Invalid email", mimetype="text/plain", status=400)

        return validate_email

    @staticmethod
    def check_user_password(func):
        @wraps(func)
        def check_password(*args, **kwargs):
            reqq = request.get_json()
            password = reqq["password"]
            user = getattr(g, 'user', None)
            print("us", user)
            # user = AuthService.find_user_by_email(email)
            with current_app.app_context():
                bcrypt = Bcrypt(current_app)
            valid = bcrypt.check_password_hash(user[4], password)
            print("val", valid)

            if valid:
                return func(*args, **kwargs)
            return Response("Incorrect password", mimetype="text/plain", status=400)

        return check_password
