import tkinter as tk


class FirstRoundFrame:
    def __init__(self, frame):
        # Set up frame structure
        self.info_frame = tk.Frame(master=frame, bg="grey", pady=5, padx=5)
        self.info_frame.pack(side="top", fill="x")
        self.refresh_frame(1)

    def refresh_frame(self, highlight=0):
        for widget in self.info_frame.winfo_children():
            widget.destroy()

        # Add numbers 1 to 15, with highlight
        for i in range(1, 16):
            if i == highlight:  # Make one number highlighted
                color = "orange"
                text_color = "red"
                font_size = 15
            else:
                color = "red"
                text_color = "white"
                font_size = 10
            circle = tk.Canvas(self.info_frame, width=30, height=30, bg="red", highlightthickness=0)
            circle.create_oval(5, 5, 25, 25, fill=color)
            circle.create_text(15, 15, text=str(i), fill=text_color, font=("Arial", font_size, "bold"))
            circle.grid(row=0, column=i - 1, padx=5)


if __name__ == "__main__":
    window = tk.Tk()
    content_frame = tk.Frame(window)
    first_round_frame = FirstRoundFrame(content_frame)
    content_frame.pack()
    window.mainloop()
