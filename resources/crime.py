import sys
from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.user import User

from models.crime import Crime


class CrimeListResource(Resource):
    def get(self):
        data = Crime.get_all()
        if data is None:
            return {'message': 'crime not found'}, HTTPStatus.NOT_FOUND
        return {'data':data}, HTTPStatus.OK
    def post(self):
        data = request.get_json()
        crime = Crime(crime_name=data['crime_name'],
                      description=data['description'])
        crime.save()
        return crime.data, HTTPStatus.CREATED
class CrimeResouces(Resource):
    def get(self,crime_id):
        crime = Crime.get_by_id(crime_id)
        if crime is None:
            return {'message': 'crime not found'}, HTTPStatus.NOT_FOUND
        return crime.data , HTTPStatus.OK
    def put(self,crime_id):
        data = request.get_json()
        return Crime.update(crime_id,data)
    def delete(self,crime_id):
        return Crime.delete(crime_id)
    
