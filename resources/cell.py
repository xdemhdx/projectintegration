import sys
from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.user import User
from models.cell import Cell


class CellListResource(Resource):
    def get(self):
        data = Cell.get_all()
        if data is None:
            return {'message': 'cell not found'}, HTTPStatus.NOT_FOUND
        return {'data':data}, HTTPStatus.OK
    def post(self):
        data = request.get_json()
        cell = Cell(block_number=data['block_number'],
                      max_capacity=data['max_capacity'])
        cell.save()
        return cell.data, HTTPStatus.CREATED
class CellResouces(Resource):
    def get(self,cell_id):
        cell = Cell.get_by_id(cell_id)
        if cell is None:
            return {'message': 'cell not found'}, HTTPStatus.NOT_FOUND
        return cell.data , HTTPStatus.OK
    def put(self,cell_id):
        data = request.get_json()
        return Cell.update(cell_id,data)
    def delete(self,cell_id):
        return Cell.delete(cell_id)
    
