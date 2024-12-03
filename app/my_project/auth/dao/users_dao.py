from flask import current_app
from my_project.auth.domain.users_domain import User
import MySQLdb.cursors

class UserDAO:
    @staticmethod
    def get_all_users():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM Users")
        users = [User(*row).to_dict() for row in cursor.fetchall()]
        cursor.close()
        return users
    
    @staticmethod
    def get_user_by_id(user_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE user_id = %s", (user_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return User(*row).to_dict()
        return None
    
    @staticmethod
    def get_users_courses():
        cursor = current_app.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        query = """
            SELECT 
                u.user_id,
                u.name AS user_name,
                c.course_id,
                c.titel_course,
                c.description_course,
                c.duration_course
            FROM 
                Users u
            JOIN 
                Enrollments e ON u.user_id = e.user_id
            JOIN 
                Courses c ON e.course_id = c.course_id
            ORDER BY 
                u.user_id;
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        users_courses = {}
        for row in rows:
            user_key = row['user_id']
            course_data = {
                'course_id': row['course_id'],
                'titel_course': row['titel_course'],
                'description_course': row['description_course'],
                'duration_course': row['duration_course'],
            }
            if user_key not in users_courses:
                users_courses[user_key] = {
                    'user_name': row['user_name'],
                    'courses': []
                }
            users_courses[user_key]['courses'].append(course_data)

        cursor.close()
        return users_courses

    @staticmethod
    def add_user(name, email, phone_number, registration_date):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO Users (name, email, phone_number, registration_date) VALUES (%s, %s, %s, %s)",
            (name, email, phone_number, registration_date)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_user(user_id, name, email, phone_number, registration_date):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "UPDATE Users SET name = %s, email = %s, phone_number = %s, registration_date = %s WHERE user_id = %s",
            (name, email, phone_number, registration_date, user_id)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete_user(user_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("DELETE FROM Users WHERE user_id = %s", (user_id,))
        current_app.mysql.connection.commit()
        cursor.close()