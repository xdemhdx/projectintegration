import sys
from extensions import db
from resources.user import UserListResource
from models.user import User
from http import HTTPStatus
from models.crime import Crime
from models.prisoner import Prisoner
from datetime import date



class PrisonerCrime(db.Model):
    __tablename__ = 'prisonercrime'
    id = db.Column(db.Integer, primary_key=True)
    prisoner_id = db.Column(db.Integer(),db.ForeignKey("prisoner.id"))
    crime_id = db.Column(db.Integer(),db.ForeignKey("crime.id"))
    cell_id = db.Column(db.Integer(),db.ForeignKey("cell.id"))
    date_committed = db.Column(db.Date(),nullable=False)
    date_incarcerated =db.Column(db.Date(),nullable=False)
    release_date = db.Column(db.Date(),nullable=True)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def data(self):
        return{
            'id': self.id,
              'prisoner_id': self.prisoner_id,
              'crime_id': self.crime_id,
              'cell_id':self.cell_id,
              'date_committed': self.date_committed.isoformat() if isinstance(self.date_committed , date) else self.date_committed,
              'date_incarcerated': self.date_incarcerated.isoformat() if isinstance(self.date_incarcerated, date) else self.date_incarcerated,
               'release_date': self.release_date.isoformat() if isinstance(self.release_date, date) else self.release_date
            
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
        pcrime = cls.query.filter(cls.id==id).first()
        if pcrime is None:
            return {"Message":"Prisoner crime not found"}
        pcrime.release_date = data['release_date']
        db.session.commit()
        return pcrime.data , HTTPStatus.OK
    @classmethod
    def delete(cls,id):
        pcrime = cls.query.filter(cls.id==id).first()
        if pcrime is None:
            return {'message':'Prisoner Crime not found'},HTTPStatus.NOT_FOUND
        db.session.delete(pcrime)
        db.session.commit()
    
    
    
