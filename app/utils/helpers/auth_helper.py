import jwt
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
secret = os.getenv("SECRET")


class AuthHelper:

    @staticmethod
    def generate_token(payload):
        print("pl", payload)
        token = jwt.encode({"id": payload[0], "firstname": payload[1], "lastname": payload[2],
                            "email": payload[3], "exp": datetime.utcnow() + timedelta(hours=14)}, secret)
        return token
