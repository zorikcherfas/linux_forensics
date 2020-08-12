from flask import Flask
from flask import request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/data_handler', methods = ['POST'])
def receive_data():

    if request.method == 'POST':
        data = request.args.get('data')
        return jsonify(messsage='Success', statusCode=200)

@app.route('/api/file_handler', methods = ['POST'])

    if request.method == 'POST':
        data = request.args.get('language')
        return jsonify(messsage='Success', statusCode=201)