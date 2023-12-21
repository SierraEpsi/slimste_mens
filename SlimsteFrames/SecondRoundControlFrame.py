import tkinter as tk


class SecondRoundControlFrame:
    def __init__(self, frame, controller, answers):
        self.controller = controller
        self.upper_frame = tk.Frame(
            master=frame,
            bg="grey")
        self.lower_frame = tk.Frame(
            master=frame,
            bg="red")

        self.upper_frame.pack(side="top", fill="x")
        self.lower_frame.pack(side="bottom", fill="x")

        answer_button = tk.Button(self.upper_frame, text=answers[0]['answer'], command=lambda: self.reveal_answer(0))
        answer_button.grid(row=0, column=0, padx=5, pady=5)
        answer_button = tk.Button(self.upper_frame, text=answers[1]['answer'], command=lambda: self.reveal_answer(1))
        answer_button.grid(row=1, column=0, padx=5, pady=5)
        answer_button = tk.Button(self.upper_frame, text=answers[2]['answer'], command=lambda: self.reveal_answer(2))
        answer_button.grid(row=2, column=0, padx=5, pady=5)
        answer_button = tk.Button(self.upper_frame, text=answers[3]['answer'], command=lambda: self.reveal_answer(3))
        answer_button.grid(row=3, column=0, padx=5, pady=5)
        self.create_start_playing()

    def create_start_playing(self):
        for widget in self.lower_frame.winfo_children():
            widget.destroy()
        start_button = tk.Button(self.lower_frame, text="Start", command=self.start)
        start_button.pack(side="left", padx=5, pady=5)

    def create_pass_playing(self):
        for widget in self.lower_frame.winfo_children():
            widget.destroy()
        pass_button = tk.Button(self.lower_frame, text="Pass", command=self.pass_question)
        pass_button.pack(side="left", padx=5, pady=5)

    def create_next_playing(self):
        for widget in self.lower_frame.winfo_children():
            widget.destroy()
        next_player_button = tk.Button(self.lower_frame, text="Start next", command=self.next_player)
        next_player_button.pack(side="left", padx=5, pady=5)

    def create_next_question(self):
        for widget in self.lower_frame.winfo_children():
            widget.destroy()
        next_question = tk.Button(self.lower_frame, text="Next question", command=self.next_question)
        next_question.pack(side="left", padx=5, pady=5)

    def reveal_answer(self, answer_nb):
        self.controller.reveal_answer_2(answer_nb)

    def start(self):
        self.controller.start_question_2()
        self.create_pass_playing()

    def pass_question(self):
        self.controller.pass_question_2()
        if self.controller.have_all_players_answered():
            self.create_next_question()
        else:
            self.create_next_playing()

    def next_player(self):
        self.controller.continue_question_2()
        self.create_pass_playing()

    def next_question(self):
        if not self.controller.have_all_players_played():
            self.controller.next_question_2()
            self.create_start_playing()
