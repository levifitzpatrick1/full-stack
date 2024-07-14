import os
import uuid
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_cors import CORS

basedirectory = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedirectory, ".env"))

guid = uuid.uuid4()


class Config:
    # This is used by flask to sign session cookies. defaults to a uinique id
    SECRET_KEY = os.environ.get("SECRET_KEY") or "guid"
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

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)

# TODO: This needs to get figured out, maybe throw it in the .env? not sure what the real response to this is.
# could just be from databoi.win once this is actually hosted there
CORS(app, resources={r"/*": {"origins": "*"}})
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# env = os.getenv("FLASK_ENV", "development")

# if env == "production":
#     app.config.from_object(ProductionConfig)
# elif env == "testing":
#     app.config.from_object(TestingConfig)
# else:
#     app.config.from_object(DevelopmentConfig)
