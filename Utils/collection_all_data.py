#import sensor collectors
from Sensor_Collectors.humidity_sensor import HumiditySensor
from Sensor_Collectors.location_sensor import LocationSensor
from Sensor_Collectors.pressure_sensor import PressureSensor
from Sensor_Collectors.temperature_sensor import TemperatureSensor
#import OpenWeather api
from API_Collectors.open_weather_api import OpenWeatherAPI

def collectAllData(msg, config, sense, room, **kwargs): #agregar parametro sense hat para los sensores sensehat y la location
    msg_copy = msg
    for collector_name, collector_object in kwargs.items():
        if isinstance(collector_object, HumiditySensor) or isinstance(collector_object, PressureSensor) or isinstance(collector_object, TemperatureSensor):
            #print('Is an instance of Humidity Sensor/Pressure Sensor/Temperature Sensor and you have to use sense Hat')
            msg_copy = collector_object.set_data(msg_copy, sense)
        elif isinstance(collector_object, OpenWeatherAPI):
            msg_copy = collector_object.get_data(msg_copy, config['city']['name'], config['open_weather']['appid'], config['open_weather']['units'])
        elif isinstance(collector_object, LocationSensor):
            msg_copy = collector_object.set_data(msg, room)
        else:
            msg_copy = collector_object.set_data(msg)
    return msg_copy