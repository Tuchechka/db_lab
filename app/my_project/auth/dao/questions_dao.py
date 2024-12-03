from flask import current_app
from my_project.auth.domain.questions_domain import Question

class QuestionDAO:
    @staticmethod
    def get_all_questions():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM Questions")
        questions = [Question(*row).to_dict() for row in cursor.fetchall()]
        cursor.close()
        return questions
    
    @staticmethod
    def get_question_by_id(question_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM Questions WHERE question_id = %s", (question_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Question(*row).to_dict()
        return None

    @staticmethod
    def add_question(test_id, text, number_points):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO Questions (test_id, text, number_points) VALUES (%s, %s, %s)",
            (test_id, text, number_points)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update_question(question_id, test_id, text, number_points):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(
            "UPDATE Questions SET test_id = %s, text = %s, number_points = %s WHERE question_id = %s",
            (test_id, text, number_points, question_id)
        )
        current_app.mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete_question(question_id):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("DELETE FROM Questions WHERE question_id = %s", (question_id,))
        current_app.mysql.connection.commit()
        cursor.close()