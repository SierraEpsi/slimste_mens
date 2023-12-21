import tkinter as tk

from SlimsteFrames.FifthRoundControlFrame import FifthRoundControlFrame
from SlimsteFrames.FinalRoundControlFrame import FinalRoundControlFrame
from SlimsteFrames.FourthRoundControlFrame import FourthRoundControlFrame
from SlimsteFrames.SecondRoundControlFrame import SecondRoundControlFrame
from SlimsteFrames.SetupFrame import SetupFrame
from SlimsteFrames.FirstRoundControlFrame import FirstRoundControlFrame
from SlimsteFrames.ThirdRoundControlFrame import ThirdRoundControlFrame


class ControlWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizz Controller")
        self.controller = None
        self.candidate_entries = None
        self.control_frame = None

        self.left_frame = tk.Frame(
            master=self.window,
            bg="red", width=200, height=500)
        self.right_frame = tk.Frame(
            master=self.window,
            bg="grey", width=500, height=500)

        self.left_frame.pack(side="left", fill="y")
        self.right_frame.pack(side="right", fill="y")

        # add round buttons to side frame
        rounds = ["Setup", "3-6-9", "Open deur", "Puzzel ronde", "Gallerij", "Collectief geheugen", "Finale"]
        self.round_buttons = [
            tk.Button(
                self.left_frame,
                text=round_name,
                command=lambda r=round_name: self.switch_round(r),
                bg="red",
                fg="black",
                font=("Helvetica", 12, "bold")
            ) for round_name in rounds
        ]
        for i, button in enumerate(self.round_buttons):
            button.grid(row=i, column=0, sticky="ew", pady=5, padx=10)

    def set_controller(self, controller):
        self.controller = controller

    def get_control_frame(self):
        return self.control_frame

    def start(self):
        self.window.mainloop()

    def switch_round(self, round_name):
        if round_name == "Setup":
            self.create_setup()
        elif round_name == "3-6-9":
            self.create_first_round()
        elif round_name == "Open deur":
            self.create_second_round()
        elif round_name == "Puzzel ronde":
            self.create_third_round()
        elif round_name == "Gallerij":
            self.create_fourth_round()
        elif round_name == "Collectief geheugen":
            self.create_fifth_round()
        elif round_name == "Finale":
            self.create_final_round()

    def refresh(self, game_state="START"):
        self.control_frame.refresh(game_state)

    def create_setup(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        self.control_frame = SetupFrame(self.right_frame, self.controller)

    def create_first_round(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        self.control_frame = FirstRoundControlFrame(self.right_frame, self.controller)
        self.controller.start_round_1()

    def create_second_round(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        self.controller.start_round_2()
        self.control_frame = SecondRoundControlFrame(
            self.right_frame,
            self.controller,
            self.controller.get_current_question()
        )
        self.controller.refresh()

    def create_third_round(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        self.controller.start_round_3()
        self.control_frame = ThirdRoundControlFrame(
            self.right_frame,
            self.controller
        )
        self.controller.refresh()

    def create_fourth_round(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        self.controller.start_round_4()
        self.control_frame = FourthRoundControlFrame(
            self.right_frame,
            self.controller
        )
        self.controller.refresh()

    def create_fifth_round(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        self.controller.start_round_5()
        self.control_frame = FifthRoundControlFrame(
            self.right_frame,
            self.controller,
            self.controller.get_current_question()
        )
        self.controller.refresh()

    def create_final_round(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        self.controller.start_round_final()
        self.control_frame = FinalRoundControlFrame(
            self.right_frame,
            self.controller,
            self.controller.get_current_question()
        )
        self.controller.refresh()

    def setup_game(self):
        candidate_names = [entry.get() for entry in self.candidate_entries]
        self.controller.add_candidates(candidate_names)
