class BashHistory:

    def __init__(self, directory=None):
        self._directory = directory

    def collect(self):
        data = []
        if self._directory:

            with open(self._directory) as f:
                output = f.readlines()
                data.append({"filename": self._directory, "data": ''.join(output)})

        return data

    def __str__(self):
        return "BashHistory"

