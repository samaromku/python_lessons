from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "You are on the main page of another server"


if __name__ == '__main__':
    app.run(port=8991, debug=True)
