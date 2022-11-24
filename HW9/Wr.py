from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
 

# ---------- FREE API KEY examples ---------------------

owm = OWM("b28fb07aac89055e68c2ca8814fd1b76")
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
city = input("Введіть назву міста:")
observation = mgr.weather_at_place(city)
w = observation.weather

print(f"""
        В {city} є такі деталі поточної погоди:
            - Статус -          {w.detailed_status}
            - Швидкість вітру -      {w.wind()['speed']}
            - Град -             {w.wind()['deg']}
            - Вологість -        {w.humidity }
            - Максимальна Температура - {w.temperature('celsius')['temp_max']}
            - Температура -     {w.temperature('celsius')['temp']}
            - Відчувається як -      {w.temperature('celsius')['feels_like']}
            - Мінімальна температура - {w.temperature('celsius')['temp_min']}
            - Дощ -            {w.rain }
            - Індекс тепла -      {w.heat_index}
            - Хмари -          {w.clouds }
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