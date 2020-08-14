from client.collectors.Volatile_Data.collector_base import CollectorBase
import subprocess

class LogginLastInfo(CollectorBase):

    def collect(self):
        output = subprocess.check_output(['last'])
        return output
    
    def __str__(self):
        return "Loggin Last"