import os
import uuid
from dotenv import load_dotenv

basedirectory = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedirectory, ".env"))


class Config:
    # This is used by flask to sign session cookies. defaults to a uinique id
    SECRET_KEY = os.environ.get("SECRET_KEY") or uuid.uuid4()
    # Uses the .env defined database, if not given uses the local sqlite db
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedirectory, "instance/tasks.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY")
