import subprocess

from client.collectors.collector_base import CollectorBase


class DateInfo(CollectorBase):

    def collect(self):
        output = subprocess.check_output(['date'])
        return output
    
    def __str__(self):
        return "Date"