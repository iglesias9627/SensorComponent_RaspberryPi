from .abstract_sensor import AbstractSensor

class LocationSensor(AbstractSensor):
    def __init__(self, name):
        super().__init__(name)
    
    def set_data(self, msg, locationName):
        msg['location'] = locationName
        return msg
