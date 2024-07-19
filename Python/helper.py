from flask import jsonify, Response
from config import app

def generate_response(message: str, status_code: int) -> Response:
    response = jsonify(message=message)
    response.status_code = status_code
    return response

def generate_error(message: str, status_code: int) -> Response:
    response = jsonify(error=message)
    response.status_code = status_code
    return response

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']