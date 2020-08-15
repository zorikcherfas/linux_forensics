from client.collectors.collector_base import CollectorBase
import subprocess

class InterfaceInfo(CollectorBase):

    def collect(self):
        output = subprocess.check_output(['ifconfig','-a'])
        return output
    
    def __str__(self):
        return "Interface"