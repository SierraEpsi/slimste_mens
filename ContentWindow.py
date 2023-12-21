import tkinter as tk

from SlimsteFrames.DefaultFrame import DefaultFrame
from SlimsteFrames.FifthRoundFrame import FifthRoundFrame
from SlimsteFrames.FinalCandidateFrame import FinalCandidateFrame
from SlimsteFrames.FinalRoundFrame import FinalRoundFrame
from SlimsteFrames.FourthRoundFrame import FourthRoundFrame
from SlimsteUtils.Player import Player

from SlimsteFrames.CandidateFrame import CandidateFrame
from SlimsteFrames.FirstRoundFrame import FirstRoundFrame
from SlimsteFrames.SecondRoundFrame import SecondRoundFrame
from SlimsteFrames.ThirdRoundFrame import ThirdRoundFrame


class ContentWindow:
    def __init__(self):
        self.round = 0

        self.window = tk.Tk()
        self.window.title("De slimste klinker")

        # Set up frame structure
        self.upper_frame = tk.Frame(
            master=self.window,
            bg="grey", width=500, height=200)
        self.lower_frame = tk.Frame(
            master=self.window,
            bg="red", width=500, height=100)

        self.upper_frame.pack(side="top", fill="x")
        self.lower_frame.pack(side="bottom", fill="x")

        self.candidate_frame = None
        self.init_candidates([
            Player("player_1"), Player("player_2"), Player("player_3")
        ])
        self.content_frame = DefaultFrame(self.upper_frame)

    def start(self):
        self.window.mainloop()

    def get_candidate_frame(self):
        return self.candidate_frame

    def get_content_frame(self):
        return self.content_frame

    def get_window(self):
        return self.window

    def init_candidates(self, players):
        for widget in self.lower_frame.winfo_children():
            widget.destroy()
        self.candidate_frame = CandidateFrame(self.lower_frame, players)

    def init_candidates_final(self, players):
        for widget in self.lower_frame.winfo_children():
            widget.destroy()
        self.candidate_frame = FinalCandidateFrame(self.lower_frame, players)

    def refresh(self, players, current_player=-1, question_nb=-1):
        if self.round == 1:
            self.content_frame.refresh(question_nb)
        else:
            self.content_frame.refresh()
        self.candidate_frame.refresh(players, current_player)

    def create_round_1(self):
        self.round = 1
        for widget in self.upper_frame.winfo_children():
            widget.destroy()
        self.content_frame = FirstRoundFrame(self.upper_frame)

    def create_round_2(self, question):
        self.round = 2
        for widget in self.upper_frame.winfo_children():
            widget.destroy()
        self.content_frame = SecondRoundFrame(self.upper_frame, question)

    def create_round_3(self, question):
        self.round = 3
        for widget in self.upper_frame.winfo_children():
            widget.destroy()
        self.content_frame = ThirdRoundFrame(self.upper_frame, question)

    def create_round_4(self):
        self.round = 4
        for widget in self.upper_frame.winfo_children():
            widget.destroy()
        self.content_frame = FourthRoundFrame(self.upper_frame)

    def create_round_5(self, question):
        self.round = 5
        for widget in self.upper_frame.winfo_children():
            widget.destroy()
        self.content_frame = FifthRoundFrame(self.upper_frame, question)

    def create_round_final(self, question, players=-1):
        self.round = 6
        if players != -1:
            self.init_candidates_final(players)
        for widget in self.upper_frame.winfo_children():
            widget.destroy()
        self.content_frame = FinalRoundFrame(self.upper_frame, question)


if __name__ == "__main__":
    content_window = ContentWindow()
    content_window.set_up_candidate_frame([
        {"name": "test1", "score":10},
        {"name": "test2", "score":13},
        {"name": "test3", "score":12}
    ])
    content_window.start()
