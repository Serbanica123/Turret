import tkinter as tk
from gui.main_window import TurretWindow

class TurretApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Turret Control")
        
        # Load main UI window
        self.main_window = TurretWindow(self)
        self.main_window.pack()

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = TurretApp()
    app.run()