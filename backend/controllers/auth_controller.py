from flask import request, jsonify
from utils.jwt_helpers import encode_jwt
from models.user_model import get_user_by_email
from models.auth_model import mark_login, mark_logout

def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = get_user_by_email(email)
    if not user or user['password'] != password:
        return jsonify({'message': 'Invalid email or password'}), 401

    # Create JWT token
    token = encode_jwt(user['id'], user['role'])

    # Mark attendance login time
    attendance_response = mark_login(user['id'])

    return jsonify({
        'token': token,
        'user': user,
        'attendance': attendance_response
    }), 200


def logout_user():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({'message': 'Token missing or invalid'}), 401

    token = auth_header.split(" ")[1]
    from utils.jwt_helpers import decode_jwt
    payload = decode_jwt(token)
    if not payload:
        return jsonify({'message': 'Invalid or expired token'}), 401

    user_id = payload['sub']

    # Mark attendance logout time
    attendance_response = mark_logout(user_id)
    return jsonify(attendance_response), 200
