from app import create_app,db
from flask_script import Manager,Server,Shell
from flask_migrate import Migrate,MigrateCommand
from app.main.model import Admin_base


app = create_app('TestingConfig')
manage = Manager(app)   #创建manage

migrate = Migrate(app,db)

def make_shell():
    '''后期添加自己创立的数据库'''
    return dict(app=app,db=db,Admin_base=Admin_base,
                )

manage.add_command('shell',Shell(make_context=make_shell))
manage.add_command('runserver',Server(host='127.0.0.1',port='8888'))
manage.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manage.run()