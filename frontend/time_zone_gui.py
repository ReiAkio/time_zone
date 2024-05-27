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
            "Brazil/Brazilia": tk.Label(self, text="Loading"),
            "Japan/Tokyo" : tk.Label(self, text="Loading")
        }

        for label in self.city_labels.values():
            label.pack()

    def update_time(self):
        for city, label in self.city_labels.items():
            time_string = get_time(city)
            label.config(text=f"{city}: {time_string}")
        self.after(60000, self.update_time)
