import abc
class CollectorBase:

    def __init__(self):
        self._collectors = []
    
    @abc.abstractmethod
    def collect(self):
        pass
    
    @abc.abstractmethod
    def __str__(self):
        pass

    def register_collector(self, c):
        self._collectors.append(c)