from client.collectors.collector_base import CollectorBase
import subprocess

class RoutingInfo(CollectorBase):

    def collect(self):
        output = subprocess.check_output(['netstat','-rn'])
        return output
    
    def __str__(self):
        return "Routing"