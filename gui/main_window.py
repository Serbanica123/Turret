import tkinter as tk
from PIL import Image, ImageTk
import cv2
from controllers.events import on_canvas_click

class TurretWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Load and convert OpenCV image
        self.img = cv2.imread("1.png", 1)
        self.rgb_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.pil_img = Image.fromarray(self.rgb_img)
        self.img_tk = ImageTk.PhotoImage(self.pil_img)

        # Create a canvas
        self.canvas = tk.Canvas(self, width=self.img_tk.width(), height=self.img_tk.height())
        self.canvas.pack()

        # Display the image on the canvas
        self.canvas_image = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)

        # Bind mouse click event
        self.canvas.bind("<Button-1>", lambda event: on_canvas_click(event, self))

    def update_image(self):
        """ Update the image on the canvas after modification. """
        self.rgb_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.pil_img = Image.fromarray(self.rgb_img)
        self.img_tk = ImageTk.PhotoImage(self.pil_img)
        self.canvas.itemconfig(self.canvas_image, image=self.img_tk)
