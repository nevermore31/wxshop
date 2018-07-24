from app import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class Admin_base(UserMixin,db.Model):
    '''管理员基础表'''
    id = db.Column(db.Integer,primary_key=True)
    role = db.Column(db.String(10))  # 角色
    nickname = db.Column(db.String(50), nullable=True)  # 昵称
    login_name = db.Column(db.String(50), nullable=False)  # 登陆名
    password_hash = db.Column('password', db.String(100))  # 密码

    avatar = db.Column(db.String(50), nullable=True)  # 头像
    token = db.Column(db.String(50), nullable=True)  # 管理员token
    is_valid = db.Column(db.Boolean, default=True)  # 是否允许登陆
    last_edit_id = db.Column(db.Integer,nullable=True)  # 最后修改信息的管理员


    def __repr__(self):
        return '用户名称 : {}'.format(self.name)

    @property
    def password(self):
        raise AttributeError('不能获取')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self,password):
        return check_password_hash(self.password_hash,password)

