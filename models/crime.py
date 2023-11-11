import sys
from extensions import db
from resources.user import UserListResource
from models.user import User
from http import HTTPStatus


class Crime(db.Model):
    __tablename__ = 'crime'
    id = db.Column(db.Integer, primary_key=True)
    crime_name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    


    @property
    def data(self):
        return{
            'id': self.id,
              'crime_name': self.crime_name,
              'description': self.description
            
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
        crimee = cls.query.filter(cls.id==id).first()
        if crimee is None:
            return {'message':'crime not found'},HTTPStatus.NOT_FOUND
        crimee.crime_name = data['crime_name']
        crimee.description = data['description']
        db.session.commit()
        return crimee.data , HTTPStatus.OK
    @classmethod
    def delete(cls,id):
        crimee = cls.query.filter(cls.id==id).first()
        if crimee is None:
            return {'message':'crime not found'},HTTPStatus.NOT_FOUND
        db.session.delete(crimee)
        db.session.commit()
    
    
    
