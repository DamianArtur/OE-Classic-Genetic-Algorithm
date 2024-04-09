import tkinter as tk

from app.Application import Application

def on_close():
    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", on_close)
    app = Application(master=root)
    app.mainloop()