from flask import Flask
from config import DevelopmentConfig, TestingConfig, ProductionConfig
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# env = os.getenv("FLASK_ENV", "development")

# if env == "production":
#     app.config.from_object(ProductionConfig)
# elif env == "testing":
#     app.config.from_object(TestingConfig)
# else:
#     app.config.from_object(DevelopmentConfig)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":    
    app.run()
