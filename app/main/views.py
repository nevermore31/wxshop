# -*- coding:utf-8 -*-
from flask import Flask, request, make_response
from . import main_Blueprint
from app import db,admins
from flask_admin.contrib.sqla import ModelView
from .model import SuperAdmin
from flask_admin import BaseView,expose



@main_Blueprint.route('/')
def test():
    return 'APP START SUEECEES~!'

@main_Blueprint.route('/login',methods = ['POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        passwords = request.form.get('passwords')

        query = SuperAdmin.query.filter_by(adminname=user).first()
        if query is not None and query.check_password_hash(passwords):
            return 'success'
        else: return 'flase'





class AdminView(BaseView):
    @expose('/')
    def index(self):
        return self.render('/home/cqc/FLASK_ALL/wxshop/app/templates/index.html')

# admins.add_view(ModelView(SuperAdmin,db.session,name='商品'))
# admins.add_view(ModelView(Subaccount,db.session,name='商品属性名称'))
