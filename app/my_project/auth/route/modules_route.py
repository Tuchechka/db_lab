from flask import Blueprint, request
from my_project.auth.controller.modules_controller import ModuleController

api_bp = Blueprint('modules_api', __name__)

@api_bp.route('/modules', methods=['GET'])
def get_all_modules():
    return ModuleController.get_all_modules()

@api_bp.route('/modules/<int:module_id>', methods=['GET'])
def get_module(module_id):
    return ModuleController.get_module(module_id)

@api_bp.route('/modules/<int:module_id>/tests', methods=['GET'])
def get_all_modules_for_course(module_id):
    return ModuleController.get_all_tests_for_module(module_id)

@api_bp.route('/modules', methods=['POST'])
def add_module():
    data = request.get_json()
    return ModuleController.add_module(data)

@api_bp.route('/modules/<int:module_id>', methods=['PUT'])
def update_module(module_id):
    data = request.get_json()
    return ModuleController.update_module(module_id, data)

@api_bp.route('/modules/<int:module_id>', methods=['DELETE'])
def delete_module(module_id):
    return ModuleController.delete_module(module_id)
