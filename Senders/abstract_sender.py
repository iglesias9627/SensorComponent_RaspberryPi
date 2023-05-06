# senders.py
from abc import ABC, abstractmethod

class AbstractSender(ABC):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    @abstractmethod
    def send_data(self, data):
        pass