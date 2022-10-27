# home work 8, task 3 (using PyOWM API)

import weather_config

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM(weather_config.API_KEY)
mgr = owm.weather_manager()

# Getting city from an user
city = input("Enter your city name: ")

# Search for current weather in user's city and get details
observation = mgr.weather_at_place(city)
w = observation.weather

weather_parameters = {"status": w.detailed_status,  
                    "humidity": w.humidity, 
                    "clouds": w.clouds
                    }

weather_temperature = w.temperature('celsius')

if city:
    print(f"The weather details in {city} are something like this:")
    print(f"Status: {weather_parameters['status']}")
    print(f"There is level of humidity: {weather_parameters['humidity']}")
    print(f"The temperature is near {round(weather_temperature['temp'])} celsius")
    print(f"Clouds: {weather_parameters['clouds']}%")

if weather_temperature['temp'] < 15:
    tip = "It is so cold there. Put some closes as you go."
elif weather_temperature['temp'] >= 15 and weather_temperature['temp'] < 23:
    tip = "It is good temperature there. Enjoy."
else:
    tip = "It is so hot there. Stay home if possible."

print(f"Tip: {tip}")