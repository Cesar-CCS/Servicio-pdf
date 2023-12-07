import os
from dotenv import load_dotenv

load_dotenv()


class BasicConfig:
    USER_DB = os.environ['USER_DB']
    PASS_DB = os.environ['PASS_DB']
    URL_DB = os.environ['URL_DB']
    NAME_DB = os.environ['NAME_DB']
    FULL_URL_BD = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    SQLALCHEMY_DATABASE_URI = FULL_URL_BD
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    SECRET_KEY = os.environ['SECRET_KEY']
