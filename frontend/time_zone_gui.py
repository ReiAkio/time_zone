import tkinter as tk
from backend.time_city import get_time

class TimeZoneGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.update_time()

    def create_widgets(self):
        self.city_labels = {
            "America/Sao_Paulo": tk.Label(self, text="Loading"),
            "Asia/Tokyo" : tk.Label(self, text="Loading")
        }

        for label in self.city_labels.values():
            label.pack()
    
    def update_time(self):

        name_map = {
            "America/Sao_Paulo": "Akio/São Paulo",
            "Asia/Tokyo" : "Cindy/Aizu"
        }

        for city, label in self.city_labels.items():
            dt = get_time(city)
            if dt is not None:
                day = dt.day
                month = dt.month
                hour = dt.hour
                minute = dt.minute

                formatted_time = f"{name_map[city]}: dia {day} mes {month} horario: {hour:02d}:{minute:02d}"
                label.config(text=formatted_time)
                print(formatted_time)
            else:
                label.config(text="Erro ao obter horario")
        self.after(60000, self.update_time)
        
