from flask import Blueprint, request
from my_project.auth.controller.users_controller import UserController

api_bp = Blueprint('users_api', __name__)

@api_bp.route('/users', methods=['GET'])
def get_all_users():
    return UserController.get_all_users()

@api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return UserController.get_user(user_id)

@api_bp.route('/users_courses', methods=['GET'])
def get_users_courses():
    return UserController.get_users_courses()

@api_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    return UserController.add_user(data)

@api_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    return UserController.update_user(user_id, data)

@api_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return UserController.delete_user(user_id)