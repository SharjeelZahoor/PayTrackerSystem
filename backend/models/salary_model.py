from utils.helpers import get_db_connection, close_db_connection

def get_all_salaries_db():
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            SELECT 
                s.id,
                s.user_id,
                u.name AS employee_name,
                s.month_year,
                s.total_hours,
                s.extra_hours,
                s.total_pay
            FROM salaries s
            JOIN users u ON s.user_id = u.id
            ORDER BY s.id DESC;
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        raise Exception(str(e))
    finally:
        close_db_connection(connection, cursor)


def get_salary_by_user_id_db(user_id):
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            SELECT 
                s.id,
                s.user_id,
                u.name AS employee_name,
                s.month_year,
                s.total_hours,
                s.extra_hours,
                s.total_pay
            FROM salaries s
            JOIN users u ON s.user_id = u.id
            WHERE s.user_id = %s;
        """
        cursor.execute(query, (user_id,))
        return cursor.fetchall()
    except Exception as e:
        raise Exception(str(e))
    finally:
        close_db_connection(connection, cursor)
