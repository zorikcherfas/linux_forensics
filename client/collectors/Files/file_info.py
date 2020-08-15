import subprocess
from pathlib import Path


class FileInfo:

    def __init__(self):
        self._directory = None

    def collect(self):
        # printf is access date, access time, modify date, modify time,
        #           create date, create time, permissions, user id, user name,
        #           group id, group name, file size, filename and then line feed

        data = []

        for path in Path(self._directory).rglob('*'):
            output = subprocess.check_output(
                ['find', path, '-printf', "%Ax;%AT;%Tx;%TT;%Cx;%CT;%m;%U;%u;%G;%g;%s;%p\n"])

            data.append({"filename": path,
                         "data": output.decode()})

        return data

    def __str__(self):
        return "FileInfo"
