import os
import psycopg2
from dotenv import load_dotenv
from app.models import FIND_USER_BY_EMAIL, FETCH_USER

load_dotenv()
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)


class AuthService:

    @staticmethod
    def find_user_by_email(email):
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(FIND_USER_BY_EMAIL, (email,))
                user = cursor.fetchone()
        return user
        # if len(user) > 0:
        #     user_data = {"id": user[0], "firstname": user[1], "lastname": user[2], "email": user[3]}

    @staticmethod
    def find_user(email):
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(FETCH_USER, (email,))
                user = cursor.fetchone()
        return user
        # if len(user) > 0:
        #     user_data = {"id": user[0], "firstname": user[1], "lastname": user[2], "email": user[3]}

