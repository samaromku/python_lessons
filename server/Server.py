import json
from ClassTest import UserWithConstructor

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "You are on the main page"


@app.route('/test', methods=['GET', 'POST', 'DELETE'])
def test_page():
    if request.method == 'GET':
        print request.args.get("test")
        print request.args.get("anotherTest")
        return "take me to the test please"
    if request.method == 'POST':
        print request.args
        json_data = json.loads(request.data)
        user = json_data.get("user")
        user_data = UserWithConstructor(user.get('first_name'), user.get('last_name'), user.get('age'), user.get('sex'))
        print user_data
        return vars(user_data)


if __name__ == '__main__':
    app.run(port=8999, debug=True)