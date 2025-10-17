from flask import Flask
from flask_cors import CORS
import pymysql
from config import Config
from routes.routes import user_bp, attendance_bp, salary_bp 
from routes.auth_routes import auth_bp 

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
app.register_blueprint(user_bp, url_prefix="/api")
app.register_blueprint(attendance_bp, url_prefix="/api")
app.register_blueprint(salary_bp, url_prefix="/api")
app.register_blueprint(auth_bp, url_prefix="/api")
# Connect to MySQL using PyMySQL


@app.route('/')
def home():
    return "✅ Flask with PyMySQL connected successfully!"


if __name__ == '__main__':
    app.run(debug=True)
