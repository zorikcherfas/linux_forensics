from utils.message import Message
import subprocess
output = subprocess.check_output(['ifconfig', '-a'])

Message.send_message("aaa",'xxxx')
# print("iterfaces %s" % output)