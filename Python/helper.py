from typing import Dict, Tuple, Optional
from flask import jsonify

def validate_user_data(data: Dict, method: str) -> Tuple[bool, Optional[str]]:
    if method == "POST":
        required_fields = ["username"]
    elif method == "GET":
        required_fields = ["user_id"]

    empty_fields = [field for field in required_fields if not data.get(field)]
    if empty_fields:
        return False, f"Required Fields Not Provided:{', '.join(empty_fields)}"
    
    return True, None

def validate_item_data(data: Dict, method: str) -> Tuple[bool, Optional[str]]:
    if method == "POST":
        required_fields = ["item_name", "barcode", "item_link"]
    elif method == "GET":
        required_fields = ["user_id", "item_id"]
    empty_fields = [field for field in required_fields if not data.get(field)]
    if empty_fields:
        return False, f"Required Fields Not Provided: {', '.join(empty_fields)}"
    
    return True, None

def generate_response(message: str, status_code: int):
    response = jsonify(message=message), status_code
    response.status_code = status_code
    return response