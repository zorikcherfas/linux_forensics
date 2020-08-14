from utils.message import Message
from collectors.date import Date
from collectors.system_information import SystemInformation

import subprocess
output = subprocess.check_output(['ifconfig', '-a'])


collectors = []
collectors.append(Date())
collectors.append(SystemInformation())


for c in collectors:
    output = c.collect()
    Message.send_message(c,output)