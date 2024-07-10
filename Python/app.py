from modules import User, Task
from config import db, app
from flask import Flask, jsonify, request


@app.route("/user", methods=["GET", "POST"])
def user():
    if request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify(error="Invalid data"), 400

        name = data.get("name")
        if not name:
            return jsonify(error="Name is required"), 400

        email = f"{name}@gmail.com"
        user = User(name, email)
        db.session.add(user)
        db.session.commit()
        return jsonify(message="User created", user_id=user.id), 201

    elif request.method == "GET":
        user_id = request.args.get("id")
        if not user_id:
            return jsonify(error="User ID is required"), 400

        curr_user = db.session.get(User, user_id)
        if not curr_user:
            return jsonify(error="User not found"), 404

        return jsonify(user=curr_user.__repr__()), 200

    return jsonify(error="Method not allowed"), 405


@app.route("/task", methods=["POST", "GET"])
def task():
    data = request.get_json
    if request.method == "POST":
        user_id = data.get("user_id")
        title = data.get("title")
        description = data.get("description")

        if not user_id or not title or not description:
            return jsonify(error="User ID, title, and description are required"), 400

        curr_user = db.session.get(User, user_id)
        if not curr_user:
            return jsonify(error="User not found"), 404

        new_task = Task(title, description)
        curr_user.tasks.append(new_task)
        db.session.commit()
        return jsonify(message="Task created"), 201
    
    elif request.method == "GET":
        

    return jsonify(error="Method not allowed"), 405


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
