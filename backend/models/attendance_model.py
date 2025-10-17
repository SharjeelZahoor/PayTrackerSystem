from utils.helpers import get_db_connection, close_db_connection

def get_all_attendances_db():
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT 
                a.id, a.user_id, u.name AS employee_name, 
                a.work_date, a.login_time, a.logout_time, a.total_hours
            FROM attendance a
            JOIN users u ON a.user_id = u.id
            ORDER BY a.work_date DESC;
        """)
        return cursor.fetchall()
    except Exception as e:
        raise Exception(str(e))
    finally:
        close_db_connection(connection, cursor)
        
def get_one_attendance_db(user_id):
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = ("""
            SELECT 
                a.user_id, u.name AS employee_name, 
                a.work_date, a.login_time, a.logout_time, a.total_hours
            FROM attendance a
            JOIN users u ON a.user_id = u.id
            WHERE a.user_id = %s
            ORDER BY a.work_date DESC;
        """)
        cursor.execute(query, (user_id))
        return cursor.fetchall()

    except Exception as e:
        raise Exception(str(e))
    finally:
        close_db_connection(connection, cursor)  

