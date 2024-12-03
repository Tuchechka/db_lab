from flask import current_app
from my_project.auth.domain.tests_domain import Test

class TestDAO:
    @staticmethod
    def get_all_tests():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM Tests")
        tests = [Test(*row).to_dict() for row in cursor.fetchall()]
        cursor.close()
        return tests
    
    @staticmethod
    def get_test_by_id(test_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM Tests WHERE test_id = %s", (test_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Test(*row).to_dict()
        return None
    
    @staticmethod
    def get_all_questions_for_test(test_id):
        cursor = current_app.mysql.connection.cursor()
        query = """
            SELECT 
                t.titel_test AS test_title, 
                q.text AS question_text 
            FROM 
                Tests t
            LEFT JOIN 
                Questions q ON t.test_id = q.test_id
            WHERE 
                t.test_id = %s
            ORDER BY 
                q.text;
        """
        cursor.execute(query, (test_id,))
        questions = cursor.fetchall()
        cursor.close()
        return questions

    @staticmethod
    def add_test(module_id, title_test, description_test, created_date):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO Tests (module_id, titel_test, description_test, created_date) VALUES (%s, %s, %s, %s)",
            (module_id, title_test, description_test, created_date)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_test(test_id, module_id, title_test, description_test, created_date):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "UPDATE Tests SET module_id = %s, titel_test = %s, description_test = %s, created_date = %s WHERE test_id = %s",
            (module_id, title_test, description_test, created_date, test_id)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete_test(test_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("DELETE FROM Tests WHERE test_id = %s", (test_id,))
        current_app.mysql.connection.commit()
        cursor.close()