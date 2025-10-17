from flask import Blueprint
from controllers.user_controller import get_all_users_controller, get_one_user_controller
from controllers.attendance_controller import get_all_attendances, get_one_attendance
from controllers.salary_controller import get_all_salaries,  get_salary_by_user_id

user_bp = Blueprint('user_bp', __name__)
attendance_bp = Blueprint('attendance_bp', __name__)
salary_bp = Blueprint('salary_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_all_users():
    return get_all_users_controller()

@user_bp.route('/user/<int:id>', methods=['GET'])
def get_one_users(id):
    return get_one_user_controller(id)

@attendance_bp.route('/attendances', methods=['GET'])
def get_allof_attendances():
    return get_all_attendances()

@attendance_bp.route('/attendance/<int:id>', methods=['GET'])
def get_1_attendance(id):
    return get_one_attendance(id)

@salary_bp.route('/salaries', methods=['GET'])
def fetch_all_salaries():
    return get_all_salaries()

@salary_bp.route('/salary/<int:id>', methods=['GET'])
def fetch_salary_by_user_id(id):
    return get_salary_by_user_id(id)
