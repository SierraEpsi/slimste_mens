import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

class VideoPlayerWindow:
    def __init__(self, master, video_path):
        self.master = master
        self.master.title("Video Player")

        self.video_path = video_path

        # Create video player
        self.create_video_player()

    def create_video_player(self):
        self.video_frame = tk.Frame(self.master)
        self.video_frame.pack()

        self.canvas = tk.Canvas(self.video_frame)
        self.canvas.pack()

        # Open the video file
        self.cap = cv2.VideoCapture(self.video_path)

        # Get the video properties
        self.width = int(self.cap.get(3))
        self.height = int(self.cap.get(4))

        # Set up tkinter window to show video
        self.canvas.config(width=self.width, height=self.height)

        # Play the video
        self.play_video()

    def play_video(self):
        ret, frame = self.cap.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.master.after(10, self.play_video)
        else:
            self.show_message("Video End", "The video has ended.")
            self.cap.release()

    def show_message(self, title, message):
        tk.messagebox.showinfo(title, message)

# Example video path (replace with your video file path)
video_path = "path/to/your/video.mp4"

# Create the main window
root = tk.Tk()
video_player_window = VideoPlayerWindow(root, video_path)
root.mainloop()
