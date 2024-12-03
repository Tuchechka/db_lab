from flask import Blueprint, request
from my_project.auth.controller.tests_controller import TestController

api_bp = Blueprint('tests_api', __name__)

@api_bp.route('/tests', methods=['GET'])
def get_all_tests():
    return TestController.get_all_tests()

@api_bp.route('/tests/<int:test_id>', methods=['GET'])
def get_test(test_id):
    return TestController.get_test(test_id)

@api_bp.route('/tests/<int:test_id>/questions', methods=['GET'])
def get_all_questions_for_test(test_id):
    return TestController.get_all_questions_for_test(test_id)

@api_bp.route('/tests', methods=['POST'])
def add_test():
    data = request.get_json()
    return TestController.add_test(data)

@api_bp.route('/tests/<int:test_id>', methods=['PUT'])
def update_test(test_id):
    data = request.get_json()
    return TestController.update_test(test_id, data)

@api_bp.route('/tests/<int:test_id>', methods=['DELETE'])
def delete_test(test_id):
    return TestController.delete_test(test_id)