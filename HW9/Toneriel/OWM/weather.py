import tkinter as tk
import requests
import time
from PIL import Image, ImageTk
from io import BytesIO
from api_key import api_key


def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + api_key

    global icon

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    iconss = json_data['weather'][0]['icon']
    url = 'http://openweathermap.org/img/wn/' + iconss + '.png'
    # after receving the desired icon we have to download it in order to display
    # its can be implemented by giving argument stream=TRUE
    icon_response = requests.get(url, stream=True)
    img_data = icon_response.content
    # The ImageTk module contains support to create and modify
    # Tkinter BitmapImage and PhotoImage objects from PIL images
    icon = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%S", time.gmtime(
        json_data['sys']['sunrise']+10800))
    sunset = time.strftime("%H:%M:%S", time.gmtime(
        json_data['sys']['sunset']+10800))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Pressure: " + str(
        pressure) + " hPa" + "\n" + "Humidity: " + str(humidity) + '%' + "\n" + "Wind Speed: " + str(wind) + " m/s" + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset

    label.configure(image=icon)
    label1.configure(text=final_info)
    label2.configure(text=final_data)


canvas = tk.Tk()
canvas.geometry("450x450")
canvas.title("Weather App")
canvas.configure()

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label = tk.Label(canvas)
label.pack()
label1 = tk.Label(canvas, font=f)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()


canvas.mainloop()
