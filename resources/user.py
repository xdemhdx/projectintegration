from flask import request
from flask_restful import Resource
from http import HTTPStatus

from utils import hash_password
from models.user import User


class UserListResource(Resource):
    def post(self):
        json_data = request.get_json()
        email = json_data.get('email')
        non_hash_password = json_data.get('password')          
        if User.get_by_email(email):
            return {'message': 'email already used'}, HTTPStatus.BAD_REQUEST

        password = hash_password(non_hash_password)

        user = User(
            email=email,
            password=password
        )

        user.save()

        data = {
            'id': user.id,
            'email': user.email
        }

        return data, HTTPStatus.CREATED
