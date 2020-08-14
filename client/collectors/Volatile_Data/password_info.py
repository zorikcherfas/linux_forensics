from client.collectors.Volatile_Data.collector_base import CollectorBase
import subprocess

class PasswordInfo(CollectorBase):

    def collect(self):
        output = subprocess.check_output(['cat','/etc/passwd'])
        return output
    
    def __str__(self):
        return "Loggin Last"