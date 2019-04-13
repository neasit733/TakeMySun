from tkinter import *
from tkinter import messagebox as mb #блять, потому что так легче писать
import time
import locale
import pyowm

window = Tk()
window.title("TsikaWeather")
weight = window.winfo_screenwidth()//2 - 300
height = window.winfo_screenheight()//2 - 300
window.geometry('335x500+{}+{}'.format(weight, height))


owm = pyowm.OWM(API_key="f61564d6483322c50316ab46ed520830", language='ru')

locale.setlocale(locale.LC_ALL, "Russian_Russia.1251")
date = "%x"
t = time.strftime(date)


def weather():
    s = button_entry.get()
    try:
        observation = owm.weather_at_place(s)
    except :
        error = mb.showerror("Ошибка", "Введите корректное название города")
    finally:
        w = observation.get_weather()
        status = w.get_detailed_status()
        wind = w.get_wind()['speed']
        temperature = w.get_temperature('celsius')["temp"]
        mb.showinfo("Погода на " + t, "В городе " + s + " сейчас "+status + ", температура " + str(temperature) + " ℃," + " скорость ветра " + str(wind) + " м/c")

string_date = Label(text="Дата: " + t)
label_request = Label(text="Введите название города", height=1, width=22)
button_entry = Entry(width=25)
button_get_weather = Button(text='Узнать погоду!', command=weather)


string_date.place(x=0, y=0)
label_request.place(x=100, y=100)
button_entry.place(x=100, y=120)
button_get_weather.place(x=128, y=145)


window.resizable(False, False)
window.mainloop()
