import tkinter as tk

from app.Application import Application
from app.Application2 import Application2
def on_close():
    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", on_close)
    app = Application2(master=root)
    app.mainloop()