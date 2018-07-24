'''for the test'''
import requests

def login():
        data = {'username':'cqc',
                'passwords':'123456'}

        url = 'http://127.0.0.1:8888/login'
        req = requests.post(url,data=data)
        print(req.text)

def logout():
        url = 'http://127.0.0.1:8888/logout'
        req = requests.get(url)
        print(req.text)


def test():
        url = 'http://127.0.0.1:8888/test'
        req = requests.get(url)
        print(req.text)


if __name__ == '__main__':
        # login()
        # logout()
        test()