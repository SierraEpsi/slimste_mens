import tkinter as tk


class FifthRoundFrame:
    def __init__(self, frame, question):
        # Set up frame structure
        self.question = question
        self.info_frame = tk.Frame(master=frame, bg="grey", pady=5, padx=5)
        self.info_frame.pack(side="top", fill="x")
        self.refresh()

    def refresh(self):
        for widget in self.info_frame.winfo_children():
            widget.destroy()

        for i, answer in enumerate(self.question.get_answers()):
            color = "red"
            if answer.is_revealed():
                color = "white"
            label = tk.Label(
                master=self.info_frame,
                text=answer.get_answer(),
                font=("Arial", 40, "bold"),
                fg=color,
                bg="red",
                padx=10,
                pady=5,
            )
            label.grid(row=i, column=0, padx=5, pady=5)
