import random
import tkinter as tk


class ThirdRoundFrame:
    def __init__(self, frame, question):
        # Set up frame structure
        self.question = question
        self.hints = []
        for answer in self.question.get_answers():
            self.hints.extend(answer.get_hints())
        self.hints = self.shuffle_hints(self.hints)

        self.upper_frame = tk.Frame(
            master=frame,
            bg="grey")
        self.lower_frame = tk.Frame(
            master=frame,
            bg="red")

        self.upper_frame.pack(side="top", fill="x")
        self.lower_frame.pack(side="bottom", fill="x")
        self.refresh()

    @staticmethod
    def shuffle_hints(hints):
        shuffled_hints = hints.copy()
        random.shuffle(shuffled_hints)
        return shuffled_hints

    def refresh(self):
        for widget in self.upper_frame.winfo_children():
            widget.destroy()

        for i, hint in enumerate(self.hints):
            color = "white"
            if hint.is_revealed():
                color = hint.get_color()
            label = tk.Label(
                master=self.upper_frame,
                text=hint.get_hint(),
                font=("Arial", 16, "bold"),
                fg=color,
                bg="red",
                padx=10,
                pady=5,
            )
            label.grid(row=int(i/3), column=i % 3, padx=5, pady=5)

        for widget in self.lower_frame.winfo_children():
            widget.destroy()

        for i, answer in enumerate(self.question.get_answers()):
            color = "red"
            if answer.is_revealed():
                color = answer.get_color()
            label = tk.Label(
                master=self.lower_frame,
                text=answer.get_answer(),
                font=("Arial", 16, "bold"),
                fg=color,
                bg="red",
                padx=10,
                pady=5,
            )
            label.grid(row=i, column=0, padx=5, pady=5)
