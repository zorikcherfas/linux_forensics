from client.collectors.collector_base import CollectorBase
import subprocess

class MountInfo(CollectorBase):

    def collect(self):
        output = subprocess.check_output(['mount'])
        return output
    
    def __str__(self):
        return "System Information"