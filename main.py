import tkinter as tk
from frontend.time_zone_gui import TimeZoneGUI

def main():
    root = tk.Tk()
    root.title("Akio-Cindy Clock")
    app = TimeZoneGUI(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()