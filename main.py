# main.py
from sense_hat import SenseHat
import copy
from loaders.config_loader import load_config
from loaders.template_loader import load_template
#import sender
from Senders.rubycop_sender import RubyCOPSender
#import OpenWeather api
from API_Collectors.open_weather_api import OpenWeatherAPI
#import sensor collectors
from Sensor_Collectors.date_sensor import DateSensor
from Sensor_Collectors.device_sensor import DeviceSensor
from Sensor_Collectors.humidity_sensor import HumiditySensor
from Sensor_Collectors.location_sensor import LocationSensor
from Sensor_Collectors.pressure_sensor import PressureSensor
from Sensor_Collectors.temperature_sensor import TemperatureSensor
from Sensor_Collectors.time_sensor import TimeSensor
#import method to collect all data
from Utils.collection_all_data import collectAllData
#import method to show message in LED
from Utils.display_sense_hat import displayMessage

def main():
    #instance Sense Hat
    sense = SenseHat()
    #load config
    config = load_config('./config_files/config.json')
    #load template each time that I want to send data multiple times
    template = load_template('./message_templates/message_template.json')
    #create RubyCOP Sender created only once but method multiple times when move
    sender = RubyCOPSender(config['websocket']['ip'], config['websocket']['port'])
    #create Open Weather Collector created only once but method multiple times when move
    weather_collector = OpenWeatherAPI('OpenWeather', config['open_weather']['url'])
    #create Date Sensor Collector
    date_collector = DateSensor('Date collector')
    #create Device Sensor Collector
    device_collector = DeviceSensor('Raspberry Pi')
    #create Location Sensor Collector
    location_collector = LocationSensor('Home')
    #create Time Sensor Collector
    time_collector = TimeSensor('Belgium')
    #create Humidity Sensor Collector
    humidity_collector = HumiditySensor("Humidity with Sense Hat")
    #create Pressure Sensor Collector
    pressure_collector = PressureSensor("Pressure from Sense Hat")
    #create Temperature Sensor Collector
    temperature_collector = TemperatureSensor("Temperature from Sense Hat")
    
    print('You can begin to send data...')
    
    while True:
        for event in sense.stick.get_events():
            #Check if the joystick was pressed
            if event.action == "pressed":
                msg = copy.deepcopy(template)
                bg = None
                room = None
                
                if event.direction in config['rooms-direction']:
                    room = config['rooms-direction'][event.direction]['room']
                    bg = config['rooms-direction'][event.direction]['color'] #string to tuple
                    msg = collectAllData(msg, config, sense, room,
                                         weather_collector = weather_collector, 
                                         date_collector = date_collector, 
                                         device_collector = device_collector, 
                                         location_collector = location_collector, 
                                         time_collector = time_collector,
                                         humidity_collector = humidity_collector,
                                         pressure_collector = pressure_collector,
                                         temperature_collector = temperature_collector)
                    print(msg)
                    print('\n')
                    displayMessage(bg, sense)
                    #send message to sender
                    sender.send_data(msg)
                elif event.direction == 'middle':
                    print('Cleaning LED...')
                    sense.clear()
                else:
                    print('An error occurred!')

if __name__ == '__main__':
    main()