from flask import jsonify
from my_project.auth.dao.tests_dao import TestDAO
from datetime import datetime

class TestController:
    @staticmethod
    def get_all_tests():
        tests = TestDAO.get_all_tests()
        test_list = [test for test in tests]
        return jsonify(test_list)

    @staticmethod
    def get_test(test_id):
        test = TestDAO.get_test_by_id(test_id)
        if test:
            return jsonify(test)
        return jsonify({'message': 'Test not found'}), 404
    
    @staticmethod
    def get_all_questions_for_test(test_id):
        questions = TestDAO.get_all_questions_for_test(test_id)
        if questions:
            return jsonify(questions)
        return jsonify({'message': 'questions not found'}), 404

    @staticmethod
    def add_test(data):
        date_str = data['created_date']
        created_date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z").date()
        formatted_date = created_date.strftime("%Y-%m-%d")
        TestDAO.add_test(data['module_id'], data['titel_test'], data['description_test'], formatted_date)
        return jsonify({'message': 'Test added successfully!'}), 201

    @staticmethod
    def update_test(test_id, data):
        date_str = data['created_date']
        created_date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z").date()
        formatted_date = created_date.strftime("%Y-%m-%d")
        TestDAO.update_test(test_id, data['module_id'], data['titel_test'], data['description_test'], formatted_date)
        return jsonify({'message': 'Test updated successfully!'}), 200

    @staticmethod
    def delete_test(test_id):
        TestDAO.delete_test(test_id)
        return jsonify({'message': 'Test deleted successfully!'}), 200