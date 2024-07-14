from modules import User, Item
from werkzeug.utils import secure_filename
from config import db, app
from flask import jsonify, request, send_from_directory
from helper import generate_response, generate_error, allowed_file
import os
from os.path import abspath, join

@app.route('/uploads/<filename>', methods=["GET"])
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/upload-photo', methods=["POST"])
def upload_photo():
    if 'photo' not in request.files:
        return generate_error("No file attached", 400)
    
    file = request.files['photo']
    uid = request.form.get('uid')
    if not uid:
        return generate_error("uid required", 400)
    
    user = db.session.query(User).filter_by(uid=uid).first()
    if not user:
        return generate_error("user not found", 400)
    
    if file.filename == '':
        return generate_error("No selected file", 400)

        
    if file and allowed_file(file.filename):
        filename = secure_filename(uid + file.filename)
        file_path = abspath(join(app.config['UPLOAD_FOLDER'], filename))

        print(f"file_path: {file_path}")
        print(f"user.photo_path: {user.photo_path}")

        file.save(file_path)

        if user.photo_path:
            os.remove(user.photo_path)

        user.photo_path = file_path
        db.session.commit()

        return jsonify(photo=filename), 200

    return generate_error('Invalid file type', 400)

@app.route("/check-username", methods=["GET"])
def check_username():
    username = request.args.get("username")
    if not username:
        return generate_response("Username is required",  400)

    user = db.session.query(User).filter_by(username=username).first()
    if user:
        return jsonify(exists=True)
    return jsonify(exists=False)

@app.route("/confirm-username", methods=["POST"])
def confirm_username():
    data = request.get_json()
    username = data.get("username")
    uid = data.get("uid")

    if not username or not uid:
        return generate_error("Username and UID are required", 400)

    user = db.session.query(User).filter_by(uid=uid).first()
    if not user:
        user = User(username=username, uid=uid)
        db.session.add(user)
    else:
        user.username = username

    db.session.commit()
    return generate_response(f"Username confirmed, uid={user.uid}", 201)

@app.route("/user", methods=["GET"])
def get_userdata():
    uid = request.args.get('uid')
    if not uid:
        return generate_error("UID Required", 400)
    
    user = db.session.query(User).filter_by(uid=uid).first()
    if not user:
        return generate_error("User not found", 404)
    
    user_data = {
        'uid' : user.uid,
        'username' : user.username,
        'photo' : user.photo_path,
        'items' : [{"id": item.id, "item_name": item.item_name, "description": item.description, "barcode": item.barcode, "item_link": item.item_link} for item in user.items] 
    }

    return jsonify({'user' : user_data}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
