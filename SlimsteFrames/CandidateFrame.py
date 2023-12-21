import tkinter as tk


class CandidateFrame:
    def __init__(self, frame, players):
        # Set up frame structure
        self.candidate_frame_current = tk.Frame(master=frame, bg="grey")
        self.candidate_frame_info = tk.Frame(master=frame, bg="red")

        self.candidate_frame_current.pack(side="top", fill="x")
        self.candidate_frame_info.pack(side="bottom", fill="x")

        # Fill current frame
        self.current_var = tk.StringVar()
        self.current_var.set(f"Current: {players[0].get_name()}")
        self.current_label = tk.Label(
            self.candidate_frame_current,
            textvariable=self.current_var,
            font=("Arial", 16, "bold"),
            fg="orange",
            bg="red",
            padx=10,
            pady=10,
        )
        self.current_label.pack(side="left")

        self.candidate_labels = []
        self.candidate_score_vars = []
        for i, player in enumerate(players):
            score_var = tk.StringVar()
            score_var.set(f"{player.get_name()}\n{player.get_score()} seconds")
            label = tk.Label(
                self.candidate_frame_info,
                textvariable=score_var,
                font=("Arial", 12, "bold"),
                fg="white",
                bg="red",
                padx=10,
                pady=5,
            )
            label.grid(row=0, column=i, padx=5, pady=5)
            self.candidate_score_vars.append(score_var)
            self.candidate_labels.append(label)

    def update_candidates(self, players, current_player=-1):
        if current_player == -1:
            self.current_var.set("Current: ")
        else:
            self.current_var.set(f"Current: {players[current_player].get_name()}")
        for i, candidate in enumerate(players):
            self.candidate_score_vars[i].set(f"{candidate.get_name()}\n{candidate.get_score()} seconds")


if __name__ == "__main__":
    window = tk.Tk()
    content_frame = tk.Frame(window)
    candidates_frame = CandidateFrame(content_frame, [
        {"name": "test1", "score":10},
        {"name": "test2", "score":13},
        {"name": "test3", "score":12}
    ])
    content_frame.pack()
    window.mainloop()
