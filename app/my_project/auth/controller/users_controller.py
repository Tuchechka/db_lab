from flask import jsonify
from my_project.auth.dao.users_dao import UserDAO
from datetime import datetime

class UserController:
    @staticmethod
    def get_all_users():
        users = UserDAO.get_all_users()
        user_list = [user for user in users]
        return jsonify(user_list)

    @staticmethod
    def get_user(user_id):
        user = UserDAO.get_user_by_id(user_id)
        if user:
            return jsonify(user)
        return jsonify({'message': 'User not found'}), 404
    
    @staticmethod
    def get_users_courses():
        users = UserDAO.get_users_courses()
        return jsonify(users)

    @staticmethod
    def add_user(data):
        date_str = data['registration_date']
        registration_date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z").date()
        formatted_date = registration_date.strftime("%Y-%m-%d")
        UserDAO.add_user(data['name'], data['email'], data['phone_number'], formatted_date)
        return jsonify({'message': 'User added successfully!'}), 201

    @staticmethod
    def update_user(user_id, data):
        date_str = data['registration_date']
        registration_date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z").date()
        formatted_date = registration_date.strftime("%Y-%m-%d")
        UserDAO.update_user(user_id, data['name'], data['email'], data['phone_number'], formatted_date)
        return jsonify({'message': 'User updated successfully!'}), 200

    @staticmethod
    def delete_user(user_id):
        UserDAO.delete_user(user_id)
        return jsonify({'message': 'User deleted successfully!'}), 200
