import json

from flask import Flask, request, render_template

from server.ClassTest import UserWithFirstLastAgeSex

app = Flask(__name__)


@app.route('/')
def index():
    return "You are on the main page"


@app.route('/test', methods=['GET', 'POST', 'DELETE'])
def test_page():
    if request.method == 'GET':
        print(request.args.get("test"))
        print(request.args.get("anotherTest"))
        return "take me to the test please"
    if request.method == 'POST':
        print(request.args)
        json_data = json.loads(request.data)
        user = json_data.get("user")
        user_data = UserWithFirstLastAgeSex(user.get('first_name'), user.get('last_name'), user.get('age'),
                                            user.get('sex'))
        print(user_data)
        return vars(user_data)


@app.route('/user_name', methods=['GET'])
def user_name():
    if request.method == 'GET':
        user = {'username': request.args.get("user")}
        return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''


@app.route('/html_file', methods=['GET'])
def html_file():
    user = UserWithFirstLastAgeSex(request.args.get("first_name"),
                                   request.args.get("last_name"),
                                   request.args.get("age"),
                                   request.args.get("sex"))
    return render_template('test.html', title='Home', user=user)


if __name__ == '__main__':
    app.run(port=8999, debug=True)
