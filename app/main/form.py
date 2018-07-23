from flask_wtf import Form
from wtforms import SubmitField,StringField,PasswordField,BooleanField
from wtforms.validators import Required,length


class loginForm(Form):
    account = StringField('账号',validators=[Required(),length(1,64)])
    password = PasswordField('密码',validators=[Required()])
    remember_me = BooleanField('保持链接')
    submit = SubmitField('登录')
