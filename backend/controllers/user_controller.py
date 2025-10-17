from flask import jsonify
from models.user_model import get_all_users_from_db, get_one_user_from_db

def get_all_users_controller():
    try:
        users = get_all_users_from_db()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_one_user_controller(user_id):
    try:
        users = get_one_user_from_db(user_id)
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500