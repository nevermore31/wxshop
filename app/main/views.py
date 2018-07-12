# -*- coding:utf-8 -*-
from flask import Flask, request, make_response
import time
from . import main_Blueprint
from app import db,admins
from flask_admin.contrib.sqla import ModelView
from .model import Subaccount,SuperAdmin
from flask_admin import BaseView,expose

@main_Blueprint.route('/')
def test():
    return 'APP START SUEECEES~!'

class AdminView(BaseView):
    @expose('/')
    def index(self):
        return self.render('/home/cqc/FLASK_ALL/wxshop/app/templates/index.html')

admins.add_view(ModelView(Subaccount,db.session,name='商铺账号信息'))
admins.add_view(ModelView(SuperAdmin,db.session,name='管理员账号信息'))

if __name__ == '__main__':
    pass