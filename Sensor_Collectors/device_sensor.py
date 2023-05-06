import platform
from .abstract_sensor import AbstractSensor

class DeviceSensor(AbstractSensor):
    def __init__(self, name):
        super().__init__(name)
    
    def set_data(self, msg):
        device = platform.uname()
        msg['device'] = device[1]
        return msg