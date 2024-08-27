from flask import Flask, request, jsonify
import json


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/test')
def testing():
    return "Testing"

@app.route("/test2")
def test_2():
    return "Testing 2"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
