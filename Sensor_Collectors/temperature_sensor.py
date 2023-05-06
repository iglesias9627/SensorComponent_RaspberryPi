from .abstract_sensor import AbstractSensor

class TemperatureSensor(AbstractSensor):
    def __init__(self, name):
        super().__init__(name)
    
    def set_data(self, msg, senseHat):
        temperature = senseHat.get_temperature()
        temperature = round(temperature, 1)
        msg['temperature_c'] = temperature
        return msg