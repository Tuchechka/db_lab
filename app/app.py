import os
from flask import Flask
from flask_mysqldb import MySQL
from my_project.auth.route.courses_route import api_bp as courses_bp
from my_project.auth.route.users_route import api_bp as users_bp
from my_project.auth.route.tests_route import api_bp as tests_bp
from my_project.auth.route.modules_route import api_bp as modules_bp
from my_project.auth.route.questions_route import api_bp as questions_bp

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'MySQLRootPassword12'
app.config['MYSQL_DB'] = 'mydb3'
app.config['MYSQL_HOST'] = 'localhost'

app.mysql = mysql

def init_db_mysql():
    cursor = mysql.connection.cursor()
    sql_file_path = os.path.join(os.path.dirname(__file__), 'data.sql')
    
    with open(sql_file_path, 'r') as f:
        sql_commands = f.read().split(';')
        
        for command in sql_commands:
            if command.strip(): 
                cursor.execute(command)
    
    mysql.connection.commit()
    cursor.close()

app.register_blueprint(courses_bp)
app.register_blueprint(users_bp)
app.register_blueprint(tests_bp)
app.register_blueprint(modules_bp)
app.register_blueprint(questions_bp)

if __name__ == '__main__':
    app.run(debug=True)
    init_db_mysql()
