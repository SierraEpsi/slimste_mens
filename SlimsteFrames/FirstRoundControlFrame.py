import tkinter as tk


class FirstRoundControlFrame:
    def __init__(self, frame, controller):
        self.controller = controller
        self.upper_frame = tk.Frame(
            master=frame,
            bg="grey")
        self.lower_frame = tk.Frame(
            master=frame,
            bg="red")

        self.upper_frame.pack(side="top", fill="x")
        self.lower_frame.pack(side="bottom", fill="x")

        self.current_label = tk.Label(
            self.upper_frame,
            text=f"Round: {self.controller.get_current_round()}\n"
                 f"Question: {self.controller.get_current_question()}\n"
                 f"Player: {self.controller.get_current_player()}\n"
                 f"Wrongs: {self.controller.get_wrongs_answers()}\n",
            font=("Arial", 12, "bold"),
            fg="black",
            bg="white",
            padx=10,
            pady=10,
        )
        self.current_label.pack(side="left")
        self.create_playing_control()

    def update_round(self):
        for widget in self.upper_frame.winfo_children():
            widget.destroy()
        self.current_label = tk.Label(
            self.upper_frame,
            text=f"Round: {self.controller.get_current_round()}\n"
                 f"Question: {self.controller.get_current_question()}\n"
                 f"Player: {self.controller.get_current_player()}\n"
                 f"Wrongs: {self.controller.get_wrongs_answers()}\n",
            font=("Arial", 12, "bold"),
            fg="black",
            bg="white",
            padx=10,
            pady=10,
        )
        self.current_label.pack(side="left")
        if self.controller.is_playing():
            self.create_playing_control()
        else:
            self.create_non_playing_control()

    def create_playing_control(self):
        for widget in self.lower_frame.winfo_children():
            widget.destroy()
        correct_button = tk.Button(self.lower_frame, text="Correct", command=self.correct)
        incorrect_button = tk.Button(self.lower_frame, text="Incorrect", command=self.incorrect)
        correct_button.grid(row=0, column=0, padx=15, pady=15, sticky="e")
        incorrect_button.grid(row=0, column=1, padx=15, pady=15, sticky="e")

    def create_non_playing_control(self):
        for widget in self.lower_frame.winfo_children():
            widget.destroy()
        next_button = tk.Button(self.lower_frame, text="Next question", command=self.next_question)
        next_button.pack(side="left", padx=5, pady=5)

    def correct(self):
        self.controller.correct_answer_1()
        self.update_round()

    def incorrect(self):
        self.controller.wrong_answer_1()
        self.update_round()

    def next_question(self):
        self.controller.next_question_1()
        self.update_round()
