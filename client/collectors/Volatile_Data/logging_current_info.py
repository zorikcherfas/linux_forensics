from client.collectors.collector_base import CollectorBase
import subprocess

class LogginCurrentInfo(CollectorBase):

    def collect(self):
        output = subprocess.check_output(['w'])
        return output
    
    def __str__(self):
        return "Loggin Current"