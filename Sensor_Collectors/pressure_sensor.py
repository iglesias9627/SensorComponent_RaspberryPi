from .abstract_sensor import AbstractSensor

class PressureSensor(AbstractSensor):
    def __init__(self, name):
        super().__init__(name)
    
    def set_data(self, msg, senseHat):
        pressure = senseHat.get_pressure()
        pressure = round(pressure, 1)
        msg['pressure'] = pressure
        return msg