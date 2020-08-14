from client.collectors.Volatile_Data.collector_base import CollectorBase
import subprocess

class LoadableKerenlModuleInfo(CollectorBase):

    def collect(self):
        output = subprocess.check_output(['lsmod'])
        return output
    
    def __str__(self):
        return "Loadable Kernel Module"