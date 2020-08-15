from client.collectors.collector_base import CollectorBase
import subprocess

class ProcessInfo(CollectorBase):

    def collect(self):
        output = subprocess.check_output(['ps','-ef'])
        return output
    
    def __str__(self):
        return "Process"