from app import db


class SuperAdmin(db.Model):
    __tablename__ = 'superadmin'

    id = db.Column(db.Integer,primary_key=True)
    adminname = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(64))

    subaccount = db.relationship('Subaccount',backref='superadmin',lazy='dynamic')

class Subaccount(db.Model):
    __tablename__ = 'subaccount'

    id = db.Column(db.Integer,primary_key=True)
    subaccountname = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(64))

    subaccount_id = db.Column(db.String(64),db.ForeignKey('superadmin.id'))
