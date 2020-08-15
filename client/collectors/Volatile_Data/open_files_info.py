from client.collectors.collector_base import CollectorBase
import subprocess

class OpenFilesInfo(CollectorBase):

    def collect(self):
        output = subprocess.check_output(['lsof','-V'])
        return output
    
    def __str__(self):
        return "Open Files"