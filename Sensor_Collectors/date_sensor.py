from datetime import datetime
from .abstract_sensor import AbstractSensor

class DateSensor(AbstractSensor):
    def __init__(self, name):
        super().__init__(name)
    
    def set_data(self, msg):
        now = datetime.now()
        msg['date'] = now.strftime("%d/%m/%Y")
        return msg