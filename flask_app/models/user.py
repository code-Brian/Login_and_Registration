from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')

class User:
    def __init__ (self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # STATIC METHODS

    @staticmethod
    def validate_registration(user):
        is_valid = True

        if len(user['first_name']) < 3:
            flash(u'First name must be at least 3 characters', 'register')
            is_valid = False

        if len(user['last_name']) < 1:
            flash(u'Last name must be at least 1 character', 'register')
            is_valid = False

        if not EMAIL_REGEX.match(user['email']):
            flash(u'Email address is not valid', 'register')
            is_valid = False

        if User.get_user_email(user):
                flash(u'Email address is already in use', 'register')
                is_valid = False

        if not PASSWORD_REGEX.match(user['password']):
            flash(u'Password must include: length of 8 characters, one uppercase letter, one digit, and include special character.', 'register')
            is_valid = False

        if not user['password'] == user['confirm_password']:
            flash(u'Passwords entered do not match', 'register')
            is_valid = False

        return is_valid

    # CLASS METHODS

    @classmethod
    def get_user_email(cls, data):
        query = '''
        SELECT * FROM users WHERE email = %(email)s;
        '''
        result = connectToMySQL('login_registration').query_db(query,data)
        if not result:
            return False
        
        user = cls(result[0])

        return user

    def check_password(cls, data):
        query = '''
        SELECT %(email)s FROM users WHERE password = %(password)s;
        '''

        result = connectToMySQL('login_registration').query_db(query, data)
        if not result:
            return False

        user = cls(result[0])

        return user

    @classmethod
    def save(cls, data):
        query='''
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        '''

        return connectToMySQL('login_registration').query_db(query, data)
    
    @classmethod
    def get_user_by_id(cls, data):
        query='''
        SELECT * FROM users WHERE users.id = %(id)s;
        '''
        result = connectToMySQL('login_registration').query_db(query, data)
        if not result:
            return False
        
        user = cls(result[0])

        return user