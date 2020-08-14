import abc

class CollectorBase:

    @abc.abstractmethod
    def collect(self):
        pass
    
    @abc.abstractmethod
    def __str__(self):
        pass

