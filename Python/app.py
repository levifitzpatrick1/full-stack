from Python.models.user import User
from config import db, app


@app.route("/create/<name>")
def create_user(name):
    db.session.add(User(name, f"{name}@gmail.com"))
    db.session.commit()
    return "created"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
