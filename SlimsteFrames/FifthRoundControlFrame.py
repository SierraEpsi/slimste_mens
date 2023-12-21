import tkinter as tk


class FifthRoundControlFrame:
    def __init__(self, frame, controller, question):
        self.controller = controller
        self.upper_frame = tk.Frame(
            master=frame,
            bg="grey")
        self.lower_frame = tk.Frame(
            master=frame,
            bg="red")

        self.upper_frame.pack(side="top", fill="x")
        self.lower_frame.pack(side="bottom", fill="x")

        self.refresh(question)

    def refresh(self, game_state="START"):
        question = self.controller.get_current_question()
        if game_state != "FINISH":
            self.refresh_answers(game_state, question)
        if game_state == "START":
            self.create_start_playing()
        if game_state == "PLAY":
            self.create_pass_playing()
        if game_state == "PAUSE":
            self.create_next_playing()
        if game_state == "END":
            self.create_next_question()

    def refresh_answers(self, game_state, question):
        for widget in self.upper_frame.winfo_children():
            widget.destroy()

        if game_state != "PLAY" or question.get_answer(0).is_revealed():
            answer_label = tk.Label(master=self.upper_frame, text=question.get_answer(0).get_answer())
            answer_label.grid(row=0, column=0, padx=5, pady=5)
        else:
            answer_button = tk.Button(self.upper_frame, text=question.get_answer(0).get_answer(), command=lambda: self.reveal_answer(0))
            answer_button.grid(row=0, column=0, padx=5, pady=5)

        if game_state != "PLAY" or question.get_answer(1).is_revealed():
            answer_label = tk.Label(master=self.upper_frame, text=question.get_answer(1).get_answer())
            answer_label.grid(row=1, column=0, padx=5, pady=5)
        else:
            answer_button = tk.Button(self.upper_frame, text=question.get_answer(1).get_answer(), command=lambda: self.reveal_answer(1))
            answer_button.grid(row=1, column=0, padx=5, pady=5)

        if game_state != "PLAY" or question.get_answer(2).is_revealed():
            answer_label = tk.Label(master=self.upper_frame, text=question.get_answer(2).get_answer())
            answer_label.grid(row=2, column=0, padx=5, pady=5)
        else:
            answer_button = tk.Button(self.upper_frame, text=question.get_answer(2).get_answer(), command=lambda: self.reveal_answer(2))
            answer_button.grid(row=2, column=0, padx=5, pady=5)

        if game_state != "PLAY" or question.get_answer(3).is_revealed():
            answer_label = tk.Label(master=self.upper_frame, text=question.get_answer(3).get_answer())
            answer_label.grid(row=3, column=0, padx=5, pady=5)
        else:
            answer_button = tk.Button(self.upper_frame, text=question.get_answer(3).get_answer(), command=lambda: self.reveal_answer(3))
            answer_button.grid(row=3, column=0, padx=5, pady=5)

        if game_state != "PLAY" or question.get_answer(4).is_revealed():
            answer_label = tk.Label(master=self.upper_frame, text=question.get_answer(4).get_answer())
            answer_label.grid(row=4, column=0, padx=5, pady=5)
        else:
            answer_button = tk.Button(self.upper_frame, text=question.get_answer(4).get_answer(), command=lambda: self.reveal_answer(4))
            answer_button.grid(row=4, column=0, padx=5, pady=5)

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
        self.controller.reveal_answer(answer_nb)

    def start(self):
        self.controller.start_question()

    def pass_question(self):
        self.controller.pass_question()

    def next_player(self):
        self.controller.continue_question()

    def next_question(self):
        self.controller.next_question()
