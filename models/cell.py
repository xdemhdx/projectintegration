import sys
from extensions import db
from resources.user import UserListResource
from models.user import User
from http import HTTPStatus


class Cell(db.Model):
    __tablename__ = 'cell'
    id = db.Column(db.Integer, primary_key=True)
    block_number = db.Column(db.Integer, nullable=False)
    max_capacity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    


    @property
    def data(self):
        return{
            'id': self.id,
              'block_number': self.block_number,
              'max_capacity': self.max_capacity
            
        }
    def save(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_all(cls):
        r = cls.query.all()
        result = []
        for i in r:
            result.append(i.data)
        return result
    @classmethod
    def get_by_id(cls,id):
        return cls.query.filter((cls.id==id)).first()
    @classmethod
    def update(cls,id,data):
        cell = cls.query.filter(cls.id==id).first()
        if cell is None:
            return {'message':'cell not found'},HTTPStatus.NOT_FOUND
        cell.block_number = data['block_number']
        cell.max_capacity = data['max_capacity']
        db.session.commit()
        return cell.data , HTTPStatus.OK
    @classmethod
    def delete(cls,id):
        cell = cls.query.filter(cls.id==id).first()
        if cell is None:
            return {'message':'cell not found'},HTTPStatus.NOT_FOUND
        db.session.delete(cell)
        db.session.commit()
    
    
    
