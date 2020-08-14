from client.collectors.Volatile_Data.collector_base import CollectorBase
import subprocess

class ShadowInfo(CollectorBase):

    def collect(self):
        output = subprocess.check_output(['cat','/etc/shadow'])
        return output
    
    def __str__(self):
        return "Shadow"