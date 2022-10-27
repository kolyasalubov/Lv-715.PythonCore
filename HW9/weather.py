from pyowm.owm import OWM
owm = OWM('b28fb07aac89055e68c2ca8814fd1b76')
mgr = owm.weather_manager()

city = input("Enter city: ")

observation = mgr.weather_at_place(city)
print(f"Weather in {city}")
print(f"Cloudiness: {observation.weather.detailed_status}")
print(f"max temperature: {observation.weather.temperature('celsius')['temp_max']} celsius")
print(f"min temperature: {observation.weather.temperature('celsius')['temp_min']} celsius")
print(f"wind speed: {observation.weather.wind() ['speed']} m/s")
print(f"humidity: {observation.weather.humidity}")

