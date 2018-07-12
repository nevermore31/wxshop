from flask import Blueprint
import os,sys
#蓝图实例化
main_Blueprint = Blueprint('main',__name__)

from . import views,errors


