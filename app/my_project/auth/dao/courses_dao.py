from flask import current_app
from my_project.auth.domain.courses_domain import Course

class CourseDAO:
    @staticmethod
    def get_all_courses():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM Courses")
        courses = [Course(*row).to_dict() for row in cursor.fetchall()]
        cursor.close()
        return courses
    
    @staticmethod
    def get_course_by_id(course_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM Courses WHERE course_id = %s", (course_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Course(*row).to_dict()
        return None
    
    @staticmethod
    def get_all_modules_for_course(course_id):
        cursor = current_app.mysql.connection.cursor()
        query = """
            SELECT 
                c.titel_course AS course_title, 
                m.titel_module AS module_title 
            FROM 
                Courses c
            LEFT JOIN 
                Modules m ON c.course_id = m.course_id
            WHERE 
                c.course_id = %s
            ORDER BY 
                c.titel_course;
        """
        cursor.execute(query, (course_id,))
        courses = cursor.fetchall()
        cursor.close()
        return courses

    @staticmethod
    def add_course(title_course, description_course, duration_course):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO Courses (titel_course, description_course, duration_course) VALUES (%s, %s, %s)",
            (title_course, description_course, duration_course)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_course(course_id, title_course, description_course, duration_course):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "UPDATE Courses SET titel_course = %s, description_course = %s, duration_course = %s WHERE course_id = %s",
            (title_course, description_course, duration_course, course_id)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete_course(course_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("DELETE FROM Courses WHERE course_id = %s", (course_id,))
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def get_courses_by_user(user_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("""SELECT Courses.* FROM Courses
                          JOIN Enrollments ON Courses.course_id = Enrollments.course_id
                          WHERE Enrollments.user_id = %s""", (user_id,))
        courses = [Course(*row).to_dict() for row in cursor.fetchall()]
        cursor.close()
        return courses