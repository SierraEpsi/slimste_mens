import tkinter as tk


class FinalCandidateFrame:
    def __init__(self, frame, players):
        # Set up frame structure
        self.candidate_frame_left = tk.Frame(master=frame, bg="grey")
        self.candidate_frame_right = tk.Frame(master=frame, bg="grey")

        self.candidate_frame_left.pack(side="left", fill="y")
        self.candidate_frame_right.pack(side="right", fill="y")

        self.refresh(players)

    def refresh(self, players, current_player=-1):
        for widget in self.candidate_frame_left.winfo_children():
            widget.destroy()

        tk.Label(
            self.candidate_frame_left,
            text=f"{players[0].get_name()}\n{players[0].get_score()}",
            font=("Arial", 40 if current_player == 1 else 50, "bold"),
            fg="white" if current_player == 1 else "orange",
            bg="red",
            padx=10,
            pady=10,
        ).pack(side="left")

        for widget in self.candidate_frame_right.winfo_children():
            widget.destroy()

        tk.Label(
            self.candidate_frame_right,
            text=f"{players[1].get_name()}\n{players[1].get_score()}",
            font=("Arial",40 if current_player == 0 else 50, "bold"),
            fg="white" if current_player == 0 else "orange",
            bg="red",
            padx=10,
            pady=10,
        ).pack(side="left")
