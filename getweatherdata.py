import requests
import tkinter as tk
from PIL import ImageTk,Image
from io import BytesIO

with open('openweathermapapikey.txt', 'r') as reader:
    api_key = reader.read()

class Application(tk.Frame):

    def __init__(self, master= None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        name_var=tk.StringVar()
        self.weather_button = tk.Button(self)
        self.location_name = tk.Label(self,text="location", font=('calibre',10,'bold'))
        self.location_entry = tk.Entry(self,textvariable=name_var,font=('calibre',10,'bold'))
        print(name_var)
        self.weather_button["text"] = "Get Weather From:\n(click me)"
        self.weather_button["command"] = self.get_weather
        self.weather_button.pack(side='top')
        self.location_entry.place(x=50,y=300)
        self.location_name.place(x=0,y=300)
        self.location_entry.pack()
        self.location_name.pack()
        self.clear = tk.Button(self,text="Clear Current Weather", command=self.clear_weather)
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side='bottom')
        self.clear.pack(side='bottom')

    def clear_weather(self):
        self.img1.destroy()
        self.weather_description.destroy()
        self.temp.destroy()

    def get_weather(self):
        city = self.location_entry.get()
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid='+ api_key+ '&main.temp="Celsius"')
        weatherData = response.json()
        print(weatherData)
        icon = weatherData['weather'][0]['icon']
        description = weatherData['weather'][0]['description']
        temp = weatherData['main']['temp']
        print(icon)
        response = requests.get('http://openweathermap.org/img/wn/'+ icon +'@2x.png')
        print(response.status_code)
        render2 = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
        self.img1 = tk.Label(self,text='weathericon',image=render2)
        self.img1.image = render2
        self.img1.place(x=100,y=100)
        self.img1.pack()
        self.weather_description = tk.Label(self,text=description, font=('calibre',10,'bold'))
        self.temp = tk.Label(self,text=temp, font=('calibre',10,'bold'))
        self.weather_description.pack(side='left')
        self.temp.pack(side='left')
        self.weather_button["text"] = "Weather"

root = tk.Tk()
root.geometry("500x400")
app = Application(master=root)

app.mainloop()

