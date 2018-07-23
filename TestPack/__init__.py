'''for the test'''
import requests


data = {'username':'cqc',
        'passwords':'123456'}

url = 'http://127.0.0.1:8888/login'
req = requests.post(url,data=data)
print(req.text)




