from flask import Blueprint, request
from my_project.auth.controller.courses_controller import CourseController

api_bp = Blueprint('courses_api', __name__)

@api_bp.route('/courses', methods=['GET'])
def get_all_courses():
    return CourseController.get_all_courses()

@api_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    return CourseController.get_course(course_id)

@api_bp.route('/courses/<int:course_id>/modules', methods=['GET'])
def get_all_modules_for_course(course_id):
    return CourseController.get_all_modules_for_course(course_id)

@api_bp.route('/courses-users/<int:users_id>', methods=['GET'])
def get_courses_by_user(users_id):
    return CourseController.get_courses_by_user(users_id)

@api_bp.route('/courses', methods=['POST'])
def add_course():
    data = request.get_json()
    return CourseController.add_course(data)

@api_bp.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    data = request.get_json()
    return CourseController.update_course(course_id, data)

@api_bp.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    return CourseController.delete_course(course_id)