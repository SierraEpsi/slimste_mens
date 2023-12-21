import tkinter as tk
from PIL import Image, ImageTk  # Import from the Pillow library


class FourthRoundFrame:
    def __init__(self, frame):
        image_path = "images/intro.jpg"
        self.image = Image.open(image_path)
        self.image = ImageTk.PhotoImage(self.image)

        self.image_label = tk.Label(frame, image=self.image)
        self.image_label.pack()

    def refresh(self):
        pass
