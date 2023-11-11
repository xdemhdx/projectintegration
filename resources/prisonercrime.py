import sys
from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.user import User
from models.cell import Cell
from models.prisoner import Prisoner
from models.prisonercrime import PrisonerCrime
from models.crime import Crime


class PrisonerCrimeListResource(Resource):
    def get(self):
        data = PrisonerCrime.get_all()
        if data is None:
            return {'message': 'Prisoners Crime not found'}, HTTPStatus.NOT_FOUND
        return {'data':data}, HTTPStatus.OK
    def post(self):
        data = request.get_json()
        prisoner_id = data['prisoner_id']
        prisoner_id = Prisoner.get_by_id(prisoner_id)
        crime_id = data['crime_id']
        crime_id = Crime.get_by_id(crime_id)
        cell_id = data['cell_id']
        cell_id = Cell.get_by_id(cell_id)
        if crime_id is None or prisoner_id is None or cell_id is None:
            return {'message': 'prisoner or crime doesnt exist'}, HTTPStatus.NOT_FOUND
        pcrime = PrisonerCrime(prisoner_id=data['prisoner_id'],
                               crime_id=data['crime_id'],
                               date_committed=data['date_committed'],
                                date_incarcerated=data['date_incarcerated'],
                                release_date=data['release_date'])
        pcrime.save()
        return pcrime.data, HTTPStatus.CREATED

class PrisonerCrimeResouces(Resource):
    def get(self,pcrime_id):
        pcrime = PrisonerCrime.get_by_id(pcrime_id)
        if pcrime is None:
            return {'message': 'prisoner crime not found'}, HTTPStatus.NOT_FOUND
        return pcrime.data , HTTPStatus.OK
    def delete(self,pcrime_id):
        return Cell.delete(pcrime_id)
    
