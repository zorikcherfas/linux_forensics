import requests

class Message:
    
    server_ip = "127.0.0.1"
    server_port = 5000
    success_code = 200

    @classmethod
    def send_message(cls, sender: str, data: str):
        url = 'http://%s:%d/api/data_handler' % (cls.server_ip, cls.server_port)
        message = {'sender': sender, 'data': data}
        result = requests.post(url, message)
        if result.status_code != cls.success_code:
            print("Message cannot be send")
