import subprocess

from client.collectors.collector_base import CollectorBase


class ConnectionInfo(CollectorBase):

    def collect(self):
        output = subprocess.check_output(['netstat','-anp'])
        return output
    
    def __str__(self):
        return "Connection"