# models/attendance_model.py
from utils.helpers import get_db_connection, close_db_connection

def mark_login(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = """
            INSERT INTO attendance (user_id, work_date, login_time)
            VALUES (%s, CURDATE(), NOW());
        """
        cursor.execute(query, (user_id,))
        connection.commit()
        return {"message": "Login time recorded successfully"}
    except Exception as e:
        connection.rollback()
        return {"error": str(e)}
    finally:
        close_db_connection(connection, cursor)


def mark_logout(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = """
            UPDATE attendance
            SET logout_time = NOW(),
                total_hours = TIMESTAMPDIFF(HOUR, login_time, NOW())
            WHERE user_id = %s AND work_date = CURDATE() AND logout_time IS NULL;
        """
        cursor.execute(query, (user_id,))
        if cursor.rowcount == 0:
            return {"message": "No active session found for today"}
        connection.commit()
        return {"message": "Logout time recorded successfully"}
    except Exception as e:
        connection.rollback()
        return {"error": str(e)}
    finally:
        close_db_connection(connection, cursor)
