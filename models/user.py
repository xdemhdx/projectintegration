from extensions import db

# User Attributes
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())
     # A static method to get a user data by the email
    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    @classmethod 
    def get_role(cls,email):
        user = cls.query.filter_by(email=email).first()
        return user.is_admin if user else None
    # Save the record
    def save(self):
        db.session.add(self)
        db.session.commit()
