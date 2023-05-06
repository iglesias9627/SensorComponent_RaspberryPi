# abstract_api.py
from abc import ABC, abstractmethod

class AbstractAPI(ABC):
    def __init__(self, name, url):
        self.url = url
        self.name = name

    @abstractmethod
    def get_data(self, *args, **kwargs):
        pass
