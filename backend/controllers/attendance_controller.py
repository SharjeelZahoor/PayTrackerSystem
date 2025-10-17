from flask import jsonify
from models.attendance_model import get_all_attendances_db, get_one_attendance_db

def get_all_attendances():
    try:
        records = get_all_attendances_db()
        return jsonify(records), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_one_attendance(user_id):
    try:
        records = get_one_attendance_db(user_id)
        return jsonify(records), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

