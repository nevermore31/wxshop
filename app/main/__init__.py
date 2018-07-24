from flask import Blueprint
from flask_restful import Api
import os,sys
from .views import Login


#蓝图实例化
main_Blueprint = Blueprint('main',__name__)
from . import views,errors

api = Api()
api.add_resource(Login,'/login')
