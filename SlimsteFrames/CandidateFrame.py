import tkinter as tk


class CandidateFrame:
    def __init__(self, frame, players):
        # Set up frame structure
        self.candidate_frame_current = tk.Frame(master=frame, bg="grey")
        self.candidate_frame_info = tk.Frame(master=frame, bg="red")

        self.candidate_frame_current.pack(side="top", fill="x")
        self.candidate_frame_info.pack(side="bottom", fill="x")

        self.refresh(players)

    def refresh(self, players, current_player=-1):
        for widget in self.candidate_frame_current.winfo_children():
            widget.destroy()

        tk.Label(
            self.candidate_frame_current,
            text=f"Current: {players[current_player].get_name()}" if current_player != -1 else "Current:",
            font=("Arial", 16, "bold"),
            fg="orange",
            bg="red",
            padx=10,
            pady=10,
        ).pack(side="left")

        for widget in self.candidate_frame_info.winfo_children():
            widget.destroy()

        for i, player in enumerate(players):
            tk.Label(
                self.candidate_frame_info,
                text=f"{player.get_name()}\n{player.get_score()} seconds",
                font=("Arial", 12, "bold"),
                fg="white",
                bg="red",
                padx=10,
                pady=5,
            ).grid(row=0, column=i, padx=5, pady=5)


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
