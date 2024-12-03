from flask import current_app
from my_project.auth.domain.modules_domain import Module

class ModuleDAO:
    @staticmethod
    def get_all_modules():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM Modules")
        modules = [Module(*row).to_dict() for row in cursor.fetchall()]
        cursor.close()
        return modules
    
    @staticmethod
    def get_module_by_id(module_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM Modules WHERE module_id = %s", (module_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Module(*row).to_dict()
        return None
    
    @staticmethod
    def get_all_tests_for_module(course_id):
        cursor = current_app.mysql.connection.cursor()
        query = """
            SELECT 
                m.titel_module AS module_title, 
                t.titel_test AS test_title 
            FROM 
                Modules m
            LEFT JOIN 
                Tests t ON m.module_id = t.module_id
            WHERE 
                m.module_id = %s
            ORDER BY 
                t.titel_test;
        """
        cursor.execute(query, (course_id,))
        tests = cursor.fetchall()
        cursor.close()
        return tests

    @staticmethod
    def add_module(title_module, course_id, description_module):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO Modules (titel_module, course_id, description_module) VALUES (%s, %s, %s)",
            (title_module, course_id, description_module)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_module(module_id, course_id, title_module, description_module):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "UPDATE Modules SET course_id = %s, titel_module = %s, description_module = %s WHERE module_id = %s",
            (course_id, title_module, description_module, module_id)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete_module(module_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("DELETE FROM Modules WHERE module_id = %s", (module_id,))
        current_app.mysql.connection.commit()
        cursor.close()