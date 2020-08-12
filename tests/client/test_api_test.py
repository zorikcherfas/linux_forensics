
import requests

url = 'http://127.0.0.1:5000/api/data_handler'
myobj = {'data': 'some_data'}

x = requests.post(url, myobj)

