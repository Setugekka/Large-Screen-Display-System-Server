# for sql
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class p_expert(db.Model):
    Id=db.Column(db.String(11), primary_key=True)
    Classification=db.Column(db.String(255))
    Field=db.Column(db.String(255))
    Name=db.Column(db.String(255))
    Sex=db.Column(db.String(255))
    Birthday=db.Column(db.String(255))
    Education=db.Column(db.String(255))
    Level=db.Column(db.String(255))
    Working_seniority=db.Column(db.Numeric)
    Phone=db.Column(db.String(255))
    City=db.Column(db.String(255))

class p_repair(db.Model):
    Id=db.Column(db.String(11), primary_key=True)
    Dep_name=db.Column(db.String(255))
    Per_name=db.Column(db.String(255))
    Major=db.Column(db.String(255))
    Post=db.Column(db.String(255))
    Office_num=db.Column(db.String(255))
    Phone=db.Column(db.String(255))
    City=db.Column(db.String(255))

class p_manager(db.Model):
    Id=db.Column(db.String(11), primary_key=True)
    Name=db.Column(db.String(255))
    Post=db.Column(db.String(255))
    Birthday=db.Column(db.String(255))
    Education=db.Column(db.String(255))
    Department=db.Column(db.String(255))
    Major=db.Column(db.String(255))
    Phone=db.Column(db.String(255))
    Health=db.Column(db.String(255))
    City=db.Column(db.String(255))

class m_equipment(db.Model):
    Id=db.Column(db.String(11), primary_key=True)
    Name=db.Column(db.String(255))
    Num=db.Column(db.Numeric)
    Unit=db.Column(db.String(255))
    Type=db.Column(db.String(255))
    Model=db.Column(db.String(255))
    Standard=db.Column(db.String(255))
    City=db.Column(db.String(255))

class m_urgent_stuff(db.Model):
    Id=db.Column(db.String(11), primary_key=True)
    Name=db.Column(db.String(255))
    Type = db.Column(db.String(255))
    Num=db.Column(db.Numeric)
    Unit=db.Column(db.String(255))
    Position=db.Column(db.String(255))
    Time=db.Column(db.String(255))
    Keeper = db.Column(db.String(255))
    Phone = db.Column(db.String(255))
    City=db.Column(db.String(255))


class m_urgent_material(db.Model):
    Id = db.Column(db.String(11), primary_key=True)
    Name = db.Column(db.String(255))
    Type = db.Column(db.String(255))
    Num = db.Column(db.Numeric)
    Unit = db.Column(db.String(255))
    Position = db.Column(db.String(255))
    Time = db.Column(db.String(255))
    Keeper = db.Column(db.String(255))
    Phone = db.Column(db.String(255))
    City = db.Column(db.String(255))


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


