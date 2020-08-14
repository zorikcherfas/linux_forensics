from collectors.collector_base import CollectorBase
import subprocess

class Date(CollectorBase):

    def collect(self):
        output = subprocess.check_output(['date'])
        return output
    
    def __str__(self):
        return "Date"