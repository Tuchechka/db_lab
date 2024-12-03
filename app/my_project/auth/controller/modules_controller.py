from flask import jsonify
from my_project.auth.dao.modules_dao import ModuleDAO

class ModuleController:
    @staticmethod
    def get_all_modules():
        modules = ModuleDAO.get_all_modules()
        module_list = [module for module in modules]
        return jsonify(module_list)

    @staticmethod
    def get_module(module_id):
        module = ModuleDAO.get_module_by_id(module_id)
        if module:
            return jsonify(module)
        return jsonify({'message': 'Module not found'}), 404
    
    @staticmethod
    def get_all_tests_for_module(module_id):
        tests = ModuleDAO.get_all_tests_for_module(module_id)
        if tests:
            return jsonify(tests)
        return jsonify({'message': 'tests not found'}), 404

    @staticmethod
    def add_module(data):
        ModuleDAO.add_module(data['titel_module'], data['course_id'], data['description_module'])
        return jsonify({'message': 'Module added successfully!'}), 201

    @staticmethod
    def update_module(module_id, data):
        ModuleDAO.update_module(module_id, data['course_id'], data['titel_module'], data['description_module'])
        return jsonify({'message': 'Module updated successfully!'}), 200

    @staticmethod
    def delete_module(module_id):
        ModuleDAO.delete_module(module_id)
        return jsonify({'message': 'Module deleted successfully!'}), 200
