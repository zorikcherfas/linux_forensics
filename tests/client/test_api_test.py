import requests


def test_send_data():
    url = 'http://127.0.0.1:5000/api/data_handler'
    myobj = {'data': 'some_data'}

    x = requests.post(url, myobj)


def test_send_command_ifconfig():
    import subprocess
    command = 'ifconfig -a'
    output = subprocess.check_output(command.split(' '))

    url = 'http://127.0.0.1:5000/api/data_handler'
    myobj = {'command': command,
             'data': output
             }
    x = requests.post(url, myobj)


def test_send_command_dmegs():
    import subprocess
    command = 'dmesg'
    output = subprocess.check_output(command.split(' '))

    url = 'http://127.0.0.1:5000/api/data_handler'
    myobj = {'command': command,
             'data': output
             }
    x = requests.post(url, myobj)
