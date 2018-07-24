# -*- coding:utf-8 -*-
from flask import request
from flask_admin.contrib.sqla import ModelView
from .model import Admin_base
from flask_restful import Resource
from flask_login import login_user,current_user,login_required

class Test(Resource):
    def get(self):
        return {'msg':'APP START SUEECEES~!'}


class Login(Resource):
    def post(self):
        if request.method == 'POST':
            user = request.form.get('username')
            passwords = request.form.get('passwords')
            query = Admin_base.query.filter_by(login_name=user).first()
            if query is not None and query.check_password_hash(passwords):
                login_user(query,remember=True)
                return {'Role':query.role}
            else: return {'Role':'账号或密码不正确,请检查在登录'}


@login_required
class Current_user(Resource):
    def get(self):
        pass

