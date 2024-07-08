from modules import User, Task
from config import db, app


@app.route("/create/<name>")
def create_user(name):
    db.session.add(User(name, f"{name}@gmail.com"))
    db.session.commit()
    return "created"


@app.route("/create/<id>/task/<title>/<description>")
def create_task(id, title, description):
    curr_user = db.session.get(User, id)
    new_task = Task(title, description)
    curr_user.tasks.append(new_task)
    db.session.commit()
    return "task created"


@app.route("/get/<id>")
def get_user(id):
    curr_user = db.session.get(User, id)
    return curr_user.__repr__()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
