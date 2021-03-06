from flask import Flask
from flask import request, jsonify
import logging

app = Flask(__name__)
logger = logging.getLogger("server")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
fh = logging.FileHandler('server.log')
fh.setLevel(logging.DEBUG)

logger.addHandler(ch)
logger.addHandler(fh)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/data_handler', methods = ['POST'])
def receive_data():
    if request.method == 'POST':
        sender = request.form.get('sender')
        data = request.form.get('data')
        logger.debug(sender)
        logger.debug(data)
        return jsonify(messsage='Success', statusCode=200)

@app.route('/api/file_handler', methods = ['POST'])
def receive_file():
    if request.method == 'POST':
        sender = request.form.get('sender')
        filename = request.form.get('filename')
        data = request.form.get('data')

        logger.debug(sender)
        logger.debug(filename)
        logger.debug(data)


        return jsonify(messsage='Success', statusCode=200)