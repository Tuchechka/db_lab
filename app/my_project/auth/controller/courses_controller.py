from flask import jsonify
from my_project.auth.dao.courses_dao import CourseDAO

class CourseController:
    @staticmethod
    def get_all_courses():
        courses = CourseDAO.get_all_courses()
        course_list = [course for course in courses]
        return jsonify(course_list)

    @staticmethod
    def get_course(course_id):
        course = CourseDAO.get_course_by_id(course_id)
        if course:
            return jsonify(course)
        return jsonify({'message': 'Course not found'}), 404
    
    @staticmethod
    def get_all_modules_for_course(course_id):
        courses = CourseDAO.get_all_modules_for_course(course_id)
        course_list = [course for course in courses]
        return jsonify(course_list)
    
    @staticmethod
    def get_courses_by_user(user_id):
        course = CourseDAO.get_courses_by_user(user_id)
        if course:
            return jsonify(course)
        return jsonify({'message': 'Course not found'}), 404

    @staticmethod
    def add_course(data):
        CourseDAO.add_course(data['titel_course'], data['description_course'], data['duration_course'])
        return jsonify({'message': 'Course added successfully!'}), 201

    @staticmethod
    def update_course(course_id, data):
        CourseDAO.update_course(course_id, data['titel_course'], data['description_course'], data['duration_course'])
        return jsonify({'message': 'Course updated successfully!'}), 200

    @staticmethod
    def delete_course(course_id):
        CourseDAO.delete_course(course_id)
        return jsonify({'message': 'Course deleted successfully!'}), 200
