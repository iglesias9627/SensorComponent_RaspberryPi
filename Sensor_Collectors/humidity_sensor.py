from .abstract_sensor import AbstractSensor

class HumiditySensor(AbstractSensor):
    def __init__(self, name):
        super().__init__(name)
    
    def set_data(self, msg, senseHat):
        humidity = senseHat.get_humidity()
        humidity = round(humidity, 1)
        msg['humidity'] = humidity
        return msg
