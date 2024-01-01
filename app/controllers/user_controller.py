from app.services import UserService, AuthService
from flask import current_app
from flask_bcrypt import Bcrypt
from app.utils import AuthHelper


class UserController:

    @staticmethod
    def user_signup(first_name, last_name, email, password):
        try:
            with current_app.app_context():
                bcrypt = Bcrypt(current_app)
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = UserService.create_user(first_name, last_name, email, hashed_password)
            return user
        except Exception as e:
            current_app.logger.error(e)
            return {"message": "Error while processing, it's not you it's us"}, 500

    @staticmethod
    def user_login(email):
        try:
            # with current_app.app_context():
            #     bcrypt = Bcrypt(current_app)
            # hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = AuthService.find_user_by_email(email)
            print("uu", user)
            token = AuthHelper.generate_token(user)
            print("token", token)
            data = {"data": {"id": user[0], "firstname": user[1], "lastname": user[2],
                            "email": user[3]}, "token": token}
            return data
        except Exception as e:
            current_app.logger.error(e)
            # return {"message": "Error while processing, it's not you it's us"}, 500
