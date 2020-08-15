from client.collectors.collector_base import CollectorBase
import subprocess

class SystemInfo(CollectorBase):

    def collect(self):
        output = subprocess.check_output(['uname','-a'])
        return output
    
    def __str__(self):
        return "System"