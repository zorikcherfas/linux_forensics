
import requests
class Message:
    
    server_ip = "127.0.0.1"
    server_port = 5000

    @classmethod
    def send_message(cls, sender:str , data: str):
        url = 'http://%s:%d/api/data_handler' % (cls.server_ip, cls.server_port)
        print(url)
        message = {'sender':sender, 'data': data }
        result = requests.post(url, message)
        if result.text['message'] != "Success" and result.text['errorCode'] != 200:
            print("Message cannot be send")
