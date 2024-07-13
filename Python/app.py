from modules import User, Item
from config import db, app
from flask import jsonify, request
from helper import validate_item_data, validate_user_data


@app.route("/user", methods=["GET", "POST"])
def user():
    data = request.get_json()
    valid_data, error_message = validate_user_data(data, request.method)
    if not valid_data:
        return error_message
    
    if request.method == "POST":
        validate_user_data(data)
        name = data.get("username")
        user = User(name)
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

        return jsonify(user=curr_user), 200

    return jsonify(error="Method not allowed"), 405


@app.route("/Item", methods=["POST", "GET"])
def item():
    data = request.get_json
    valid_data, error_message = validate_item_data(data, request.method)
    if not valid_data:
        return error_message
    
    if request.method == "POST":
        user_id = data.get("user_id")
        item_name = data.get("item_name")
        description = data.get("description")
        barcode = data.get("barcode")
        item_link = data.get("item_link")

        if not user_id or not item_name or not description or not barcode or not item_link:
            return jsonify(error="User ID, item_name, description, barcode, and item_link are required"), 400

        curr_user = db.session.get(User, user_id)
        if not curr_user:
            return jsonify(error="User not found"), 404

        new_item = Item(item_name, description, barcode)
        curr_user.tasks.append(new_item)
        db.session.commit()
        return jsonify(message="Task created"), 201
    
    elif request.method == "GET":
        return jsonify(error="Method not allowed"), 405


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
