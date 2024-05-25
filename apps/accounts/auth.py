from django.conf import settings  # import the settings file
from apps.accounts.models import *  # import the Jwt model
from datetime import datetime, timedelta  # import datetime and timedelta
import jwt, random, string  # import jwt, random and string

ALGORITHM = "HS256"  # set algorithm to HS256


class Authentication:  # create Authentication class
    # generate random string
    def get_random(length: int):
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))

    # generate access token based and encode user's id
    def create_access_token(payload: dict):
        expire = datetime.utcnow() + timedelta(
            minutes=int(settings.ACCESS_TOKEN_LIFETIME_MINUTES)
        )
        to_encode = {"exp": expire, **payload}
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
