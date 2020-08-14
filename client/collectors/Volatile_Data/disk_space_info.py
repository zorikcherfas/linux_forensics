from client.collectors.Volatile_Data.collector_base import CollectorBase
import subprocess

class DiskSpaceInfo(CollectorBase):

    def collect(self):
        output = subprocess.check_output(['df'])
        return output
    
    def __str__(self):
        return "Disk Space"