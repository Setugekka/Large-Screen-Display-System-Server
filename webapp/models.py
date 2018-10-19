# for sql
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import AnonymousUserMixin, UserMixin

db=SQLAlchemy()
class users(UserMixin, db.Model):
    # username = db.StringField(max_length=100, primary_key=True)
    userid=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(45))
    password = db.Column(db.String(45))

    def __init__(self, **kwargs):
        super(users, self).__init__(**kwargs)
    # def can(self, permissions):
    #     result = users_roles.query.filter_by(user_name=self.username).first()
    #     return result is not None and \
    #            result.permissions <= permissions

    # def is_administrator(self):
    #     return self.can(Permission.administrator)

    # roles = db.relationship(
    #         'Role',
    #         secondary=roles,
    #         backref=db.backref('users', lazy='dynamic')
    # )

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return unicode(self.userid)

class log(db.Model):
    ID=db.Column(db.Integer,primary_key=True)
    UserID=db.Column(db.Integer)
    Operation=db.Column(db.String(255))
    Note=db.Column(db.String(255))
    Time=db.Column(db.DateTime)

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

class m_urgent_material(db.Model):
    __tablename__='m_urgent_material'
    Id = db.Column(db.String(11), primary_key=True)
    Name=db.Column(db.String(255))
    Type=db.Column(db.String(255))
    Num=db.Column(db.Numeric)
    Unit=db.Column(db.String(255))
    Position=db.Column(db.String(255))
    Time=db.Column(db.String(255))
    Keeper=db.Column(db.String(255))
    Phone=db.Column(db.String(255))
    City=db.Column(db.String(255))


class city_id (db.Model):
    Id = db.Column(db.String(11), primary_key=True)
    Name = db.Column(db.String(255))


class plan_list(db.Model):
    Id = db.Column(db.String(11), primary_key=True)
    Name = db.Column(db.String(255))
    Belong_to = db.Column(db.String(11))
    Level = db.Column(db.String(11))

class p_city_manager(db.Model):
    Id=db.Column(db.String(11), primary_key=True)
    Name=db.Column(db.String(255))
    Post=db.Column(db.String(255))
    Birthday=db.Column(db.String(255))
    Education=db.Column(db.String(255))
    Department=db.Column(db.String(255))
    Major=db.Column(db.String(255))
    Phone=db.Column(db.String(255))
    Date_training=db.Column(db.String(255))
    City=db.Column(db.String(255))

class p_village_manager(db.Model):
    Id=db.Column(db.String(11), primary_key=True)
    Name=db.Column(db.String(255))
    Post=db.Column(db.String(255))
    Birthday=db.Column(db.String(255))
    Education=db.Column(db.String(255))
    Department=db.Column(db.String(255))
    Major=db.Column(db.String(255))
    Phone=db.Column(db.String(255))
    Date_training=db.Column(db.String(255))
    City=db.Column(db.String(255))

class m_new_equipment(db.Model):
    Id=db.Column(db.String(11), primary_key=True)
    Name=db.Column(db.String(255))
    Num=db.Column(db.Numeric)
    Unit=db.Column(db.String(255))
    Type=db.Column(db.String(255))
    Model=db.Column(db.String(255))
    City=db.Column(db.String(255))

