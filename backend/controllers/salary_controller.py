from flask import jsonify
from models.salary_model import get_all_salaries_db, get_salary_by_user_id_db

def get_all_salaries():
    try:
        salaries = get_all_salaries_db()
        return jsonify(salaries), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def get_salary_by_user_id(user_id):
    try:
        salary = get_salary_by_user_id_db(user_id)
        if not salary:
            return jsonify({"message": "No salary record found for this user"}), 404
        return jsonify(salary), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
