from flask import Blueprint
from controllers.auth_controller import login_user, logout_user
auth_bp = Blueprint('auth', __name__)

auth_bp.add_url_rule('/login', view_func=login_user, methods=['POST'])
auth_bp.add_url_rule('/logout', view_func=logout_user, methods=['POST'])
