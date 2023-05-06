from datetime import datetime
from .abstract_sensor import AbstractSensor

class TimeSensor(AbstractSensor):
    def __init__(self, name):
        super().__init__(name)
    
    def set_data(self, msg):
        now = datetime.now()
        msg['time'] = now.strftime("%H:%M:%S")
        return msg