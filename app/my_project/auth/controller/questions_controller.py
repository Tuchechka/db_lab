from flask import jsonify
from my_project.auth.dao.questions_dao import QuestionDAO

class QuestionController:
    @staticmethod
    def get_all_questions():
        questions = QuestionDAO.get_all_questions()
        question_list = [question for question in questions]
        return jsonify(question_list)

    @staticmethod
    def get_question(question_id):
        question = QuestionDAO.get_question_by_id(question_id)
        if question:
            return jsonify(question)
        return jsonify({'message': 'Question not found'}), 404

    @staticmethod
    def add_question(data):
        QuestionDAO.add_question(data['test_id'], data['text'], data['number_points'])
        return jsonify({'message': 'Question added successfully!'}), 201

    @staticmethod
    def update_question(question_id, data):
        QuestionDAO.update_question(question_id, data['test_id'], data['text'], data['number_points'])
        return jsonify({'message': 'Question updated successfully!'}), 200

    @staticmethod
    def delete_question(question_id):
        QuestionDAO.delete_question(question_id)
        return jsonify({'message': 'Question deleted successfully!'}), 200