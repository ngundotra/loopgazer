from flask import Flask, request

import json

app = Flask(__name__)

usr, pwd = 'Marco', '247'
usr_dict = {'username':usr, 'password': pwd}


@app.route('/', methods=['GET',])
def hello():
    return json.dumps(usr_dict)


@app.route('/', methods=['POST',])
def update():
    usr_dict['username'] = request.form['username']
    usr_dict['password'] = request.form['password']
    return "HENLO! You posted:\n" + json.dumps(usr_dict)

if __name__ == '__main__':
    app.run()