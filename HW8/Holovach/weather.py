from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import weather_key 

# ---------- FREE API KEY examples ---------------------

owm = OWM(weather_key.api_key)
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
city = input("Enter city's title:")
observation = mgr.weather_at_place(city)
w = observation.weather

print(f"""
        In {city} there are such current weather's details:
            - status -          {w.detailed_status}
            - wind speed -      {w.wind()['speed']}
            - deg -             {w.wind()['deg']}
            - humidity -        {w.humidity }
            - max-temperature - {w.temperature('celsius')['temp_max']}
            - temperature -     {w.temperature('celsius')['temp']}
            - feels_like -      {w.temperature('celsius')['feels_like']}
            - min-temperature - {w.temperature('celsius')['temp_min']}
            - rain -            {w.rain }
            - heat index -      {w.heat_index}
            - clouds -          {w.clouds }
        """)

# print("----------------------------------------------")
# print(w.detailed_status)         # 'clouds'
# print(w.wind())                  # {'speed': 4.6, 'deg': 330}
# print(w.humidity)                # 87
# print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# print(w.rain)                    # {}
# print(w.heat_index)              # None
# print(w.clouds)                 # 75

# Will it be clear tomorrow at this time in Milan (Italy) ?
# forecast = mgr.forecast_at_place('Milan,IT', 'daily')
# answer = forecast.will_be_clear_at(timestamps.tomorrow())