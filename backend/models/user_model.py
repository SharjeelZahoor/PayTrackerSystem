from utils.helpers import get_db_connection, close_db_connection

def get_all_users_from_db():
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT id, name, email, role, hourly_rate FROM users;"
        cursor.execute(query)
        users = cursor.fetchall()
        return users
    except Exception as e:
        raise Exception(f"Database Error: {str(e)}")
    finally:
        close_db_connection(connection, cursor)

def get_one_user_from_db(user_id):
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT id, name, email, role, hourly_rate FROM users WHERE id = %s;"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
        return user
    except Exception as e:
        raise Exception(f"Database Error: {str(e)}")
    finally:
        close_db_connection(connection, cursor)

def get_user_by_email(email):
    """
    Fetch user details using email.
    This is used for login authentication.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT * FROM users WHERE email = %s;"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        return user  # returns dict or None
    except Exception as e:
        print("❌ Error in get_user_by_email:", e)
        return None
    finally:
        close_db_connection(connection, cursor)
