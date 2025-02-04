import cv2

def on_canvas_click(event, window):
    """ Handles mouse click events on the canvas. """
    x, y = event.x, event.y
    print(f"Mouse clicked at: {x}, {y}")

    # Draw circles on the image
    cv2.circle(window.img, (x, y), 1, (0, 0, 255), 1)
    cv2.circle(window.img, (x, y), 10, (0, 0, 255), 2)

    # Update the displayed image
    window.update_image()
