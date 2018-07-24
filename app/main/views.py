# -*- coding:utf-8 -*-
from flask import request
from flask_admin.contrib.sqla import ModelView
from .model import AdminBase
from flask_restful import Resource
from flask_login import login_user,current_user,login_required,logout_user



class Test(Resource):
    decorators = [login_required]
    def get(self):
        if request.method == 'GET':
            return {'msg':'APP START SUEECEES~!'}


class Login(Resource):
    def post(self):
        if request.method == 'POST':
            user = request.form.get('username')
            passwords = request.form.get('passwords')
            query = AdminBase.query.filter_by(login_name=user).first()
            if query is not None and query.check_password_hash(passwords):
                login_user(query,remember=True)
                return {'Role':query.role}
            else: return {'Role':'账号或密码不正确,请检查在登录'}


class Logout(Resource):
    @login_required
    def get(self):
        if request.method == 'GET':
            logout_user()
            return {'msg':"logout Ok"}



class Current_user(Resource):
    @login_required
    def get(self):
        pass

