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

class Goods(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    goodsname = db.Column(db.String(120),unique=True)
    goodsattrname = db.relationship('GoodsAttributeName',backref='goods',lazy='dynamic')
    goodsiteamsku = db.relationship('GoodsIteamSku',backref='goods',lazy='dynamic')

class GoodsAttributeName(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    attrname = db.Column(db.String(120),unique=True)
    goodsattrvalue = db.relationship('GoodsAttributeValue',backref = 'goodsattributename',lazy='dynamic')
    goods_id = db.Column(db.String(64),db.ForeignKey('goods.id'))

class GoodsAttributeValue(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    '''属性编码'''
    symbol = db.Column(db.Integer,unique=True)
    attrvalue = db.Column(db.String(120),unique=True)
    goods_id = db.Column(db.String(64),db.ForeignKey('goodsattributename.id'))

class GoodsIteamSku(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    goods_id = db.Column(db.String(64),db.ForeignKey('goods.id'))
    '''组成方式'''
    attr_name = db.Column(db.Integer)
    price = db.Column(db.Float)
    stock = db.Column(db.Integer,default=0)
