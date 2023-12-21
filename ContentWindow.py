import tkinter as tk

from SlimsteUtils.Player import Player

from SlimsteFrames.CandidateFrame import CandidateFrame
from SlimsteFrames.FirstRoundFrame import FirstRoundFrame
from SlimsteFrames.SecondRoundFrame import SecondRoundFrame


class ContentWindow:
    def __init__(self):
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

        self.candidate_frame = CandidateFrame(self.lower_frame, [
            Player("player_1"), Player("player_2"), Player("player_3")
        ])
        self.content_frame = None

    def start(self):
        self.window.mainloop()

    def get_candidate_frame(self):
        return self.candidate_frame

    def get_content_frame(self):
        return self.content_frame

    def create_round_1(self):
        for widget in self.upper_frame.winfo_children():
            widget.destroy()
        self.content_frame = FirstRoundFrame(self.upper_frame)

    def create_round_2(self, answers):
        for widget in self.upper_frame.winfo_children():
            widget.destroy()
        self.content_frame = SecondRoundFrame(self.upper_frame, answers)


if __name__ == "__main__":
    content_window = ContentWindow()
    content_window.set_up_candidate_frame([
        {"name": "test1", "score":10},
        {"name": "test2", "score":13},
        {"name": "test3", "score":12}
    ])
    content_window.start()
