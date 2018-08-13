# for sql
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class Generator(db.Model):
    __tablename__='m_generator'
    Id=db.Column(db.String(11),primary_key=True)
    Department=db.Column(db.String(255))
    Type=db.Column(db.String(255))
    Capacity=db.Column(db.Integer())
    Date_Production = db.Column(db.DateTime())
    Factory = db.Column(db.String(255))
    Contact=db.Column(db.String(255))
    Phone=db.Column(db.String(255))
    Position=db.Column(db.String(255))
    Condition=db.Column(db.String(255))
    City=db.Column(db.String(255))
class Repaircar(db.Model):
    __tablename__='m_repaircar'
    Id = db.Column(db.String(11), primary_key=True)
    Department = db.Column(db.String(255))
    License_num = db.Column(db.String(255))
    Car_type = db.Column(db.String(255))
    Brand = db.Column(db.String(255))
    Purchase_date=db.Column(db.String(255))
    Oil_type=db.Column(db.String(255))
    Contact=db.Column(db.String(255))
    Phone=db.Column(db.String(255))
    City=db.Column(db.String(255))