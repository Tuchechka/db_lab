from flask import Blueprint, request
from my_project.auth.controller.questions_controller import QuestionController

api_bp = Blueprint('questions_api', __name__)

@api_bp.route('/questions', methods=['GET'])
def get_all_questions():
    return QuestionController.get_all_questions()

@api_bp.route('/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    return QuestionController.get_question(question_id)

@api_bp.route('/questions', methods=['POST'])
def add_question():
    data = request.get_json()
    return QuestionController.add_question(data)

@api_bp.route('/questions/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    data = request.get_json()
    return QuestionController.update_question(question_id, data)

@api_bp.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    return QuestionController.delete_question(question_id)
