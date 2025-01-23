from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2 

# Function to handle mouse clicks on the Tkinter canvas
def on_canvas_click(event):
    global img, canvas_image
    # Get the coordinates of the mouse click
    x, y = event.x, event.y
    print(f"Mouse clicked at: {x}, {y}")  # Print coordinates in the console
    
    cv2.circle(img,(x,y),1,(0,0,255), 1)
    cv2.circle(img,(x,y),25,(0,0,255), 1)
    # Update the displayed image
    update_image(img)

# Function to update the image displayed in the Tkinter window
def update_image(cv_img):
    # Convert OpenCV image (BGR) to RGB
    rgb_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb_img)
    img_tk = ImageTk.PhotoImage(pil_img)
    canvas.itemconfig(canvas_image, image=img_tk)
    canvas.image = img_tk  # Keep a reference to avoid garbage collection

# Driver function 
if __name__ == "__main__":
    # Create a Tkinter window
    root = Tk()
    root.title("OpenCV Image in Tkinter with Mouse Clicks")
    
    # Load the OpenCV image
    img = cv2.imread('1.png', 1)

    # Convert the OpenCV image to RGB format for displaying in Tkinter
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb_img)
    img_tk = ImageTk.PhotoImage(pil_img)

    # Create a canvas to display the image
    canvas = Canvas(root, width=img_tk.width(), height=img_tk.height())
    canvas.pack()

    # Add the image to the canvas
    canvas_image = canvas.create_image(0, 0, anchor=NW, image=img_tk)

    # Bind mouse click event to the canvas
    canvas.bind("<Button-1>", on_canvas_click)

    # Start the Tkinter main loop
    root.mainloop()
