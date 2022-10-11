from pyowm import OWM

# ---------- FREE API KEY examples ---------------------

owm = OWM('fc7fdb55277ba9a8a49ac4061aaff9d0')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
user_city = input('Enter the city of which you want to see the weather: ')
observation = mgr.weather_at_place(user_city)
w = observation.weather

wind = w.wind()

temperature = w.temperature('celsius')


print('\tToday we have', w.detailed_status)         # 'clouds'
print("\tThe wind's speed is", wind['speed'])                # {'speed': 4.6, 'deg': 330}
print('\tHumidity level is', w.humidity)       # 87
print('\tThe temperature will be', temperature['temp'])  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print('\tMax temperture:', temperature['temp_max'])
print('\tMin temperture:', temperature['temp_min'])
if w.rain == {}:
    print('\tNo rain today!')
else:
    print(f'\tThe rain will last for', w.rain['1h'], 'hours')                   # {}
w.heat_index                     # None
print('\tThe sky is filled with', w.clouds, '% of clouds')                  # 75