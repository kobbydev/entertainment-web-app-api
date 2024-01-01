import os
import psycopg2
from dotenv import load_dotenv
from app.models import CREATE_USER_TABLE, INSERT_INTO_USER

load_dotenv()
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)


class UserService:

    @staticmethod
    def create_user(first_name, last_name, email, password):
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(CREATE_USER_TABLE)
                cursor.execute(INSERT_INTO_USER, (first_name, last_name, email, password,))
                user = cursor.fetchone()
        return {"id": user[0], "firstname": user[1], "lastname": user[2], "email": user[3]}
