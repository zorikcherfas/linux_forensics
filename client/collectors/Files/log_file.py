from client.collectors.collector_base import CollectorBase

import glob
import os

class LogFileInfo(CollectorBase):

    def __init__(self):
        pass

    def collect(self):
        data = []
        files = glob.glob("/var/log/*", recursive=True)
        for file in files:
            if file.endswith(".log"):
                try:
                    with open(file) as f:
                        lines = f.readline()
                    data.append({"filename": os.path.basename(file),
                                 "data": lines})
                except PermissionError:
                    print("PermissionError for file: %s" % file)
        return data

    def __str__(self):
        return "Logfile"


