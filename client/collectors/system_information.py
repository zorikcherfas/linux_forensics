from collectors.collector_base import CollectorBase
import subprocess

class SystemInformation(CollectorBase):

    def collect(self):
        output = subprocess.check_output(['uname','-a'])
        return output
    
    def __str__(self):
        return "System Information"