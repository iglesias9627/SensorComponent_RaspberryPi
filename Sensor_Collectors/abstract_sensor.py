from abc import ABC, abstractmethod

class AbstractSensor(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def set_data(self, *args, **kwargs):
        pass