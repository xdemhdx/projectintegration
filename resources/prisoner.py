import sys
from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.user import User
from models.cell import Cell
from models.prisoner import Prisoner


class PrisonerListResource(Resource):
    def get(self):
        data = Prisoner.get_all()
        if data is None:
            return {'message': 'Prisoners not found'}, HTTPStatus.NOT_FOUND
        return {'data':data}, HTTPStatus.OK
    def post(self):
        data = request.get_json()
        prisoner = Prisoner(first_name=data['first_name'],
                      last_name=data['last_name'],
                       dob = data['dob'])
        prisoner.save()
        return prisoner.data,HTTPStatus.CREATED
class PrisonerResouces(Resource):
    def get(self,prisoner_id):
        prisoner = Prisoner.get_by_id(prisoner_id)
        if prisoner is None:
            return {'message': 'prisoner not found'}, HTTPStatus.NOT_FOUND
        return prisoner.data , HTTPStatus.OK
    def put(self,prisoner_id):
        data = request.get_json()
        return Cell.update(prisoner_id,data)
    def delete(self,prisoner_id):
        return Prisoner.delete(prisoner_id)
    
