import sys
from extensions import db
from resources.user import UserListResource
from models.user import User
from http import HTTPStatus
from models.cell import Cell
from datetime import date



class Prisoner(db.Model):
    __tablename__ = 'prisoner'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    dob = db.Column(db.Date(),nullable = False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    
    
    @property
    def data(self):
        return{
            'id': self.id,
              'first_name': self.first_name,
              'last_name': self.last_name,
              # the date formatting has been cited from stackoverflow due to returning errors in POSTMAN
            'dob': self.dob.isoformat() if isinstance(self.dob, date) else self.dob
            
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
        prisoner = cls.query.filter(cls.id==id).first()
        if prisoner is None:
            return {'message':'prisoner not found'},HTTPStatus.NOT_FOUND
        prisoner.frist_name = data['first_name']
        prisoner.last_name = data['last_name']
        db.session.commit()
        return prisoner.data , HTTPStatus.OK
    @classmethod
    def delete(cls,id):
        prisoner = cls.query.filter(cls.id==id).first()
        if prisoner is None:
            return {'message':'prisoner not found'},HTTPStatus.NOT_FOUND
        db.session.delete(prisoner)
        db.session.commit()
        
    
    
    
