from app import db
from werkzeug.security import check_password_hash, generate_password_hash

class SuperAdmin(db.Model):
    __tablename__ = 'superadmin'

    id = db.Column(db.Integer,primary_key=True)
    adminname = db.Column(db.String(64),unique=True)
    passwords = db.Column(db.String(64),nullable=False)
    _password_hash = db.Column(db.String(128),nullable=False)


    def __repr__(self):
        return '用户名称 : {}'.format(self.adminname)

    @property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self,password):
        self._password_hash = generate_password_hash(password)

    def check_password_hash(self,password):
        return check_password_hash(self.password,password)

