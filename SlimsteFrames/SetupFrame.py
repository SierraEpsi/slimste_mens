import tkinter as tk


class SetupFrame:
    def __init__(self, frame, controller):
        self.controller = controller

        # Set up frame structure
        self.info_frame = tk.Frame(master=frame, bg="grey", pady=5, padx=5)
        self.info_frame.pack(side="top", fill="x", padx=20, pady=10)

        input_frame = tk.Frame(frame)
        submit_frame = tk.Frame(frame)

        input_frame.pack(padx=20, pady=10)
        submit_frame.pack(pady=10)

        self.candidate_entries = []
        for i in range(3):
            label = tk.Label(input_frame, text=f"Player {i + 1} Name:")
            label.grid(row=i, column=0, padx=5, pady=5, sticky="e")

            entry = tk.Entry(input_frame, width=20)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.candidate_entries.append(entry)

        submit_button = tk.Button(submit_frame, text="Submit", command=self.submit_names)
        submit_button.pack()

    def submit_names(self):
        player_names = [name.get() for name in self.candidate_entries]
        print("ADDING PLAYERS:", player_names)
        self.controller.add_candidates(player_names)


if __name__ == "__main__":
    window = tk.Tk()
    content_frame = tk.Frame(window)
    setup_frame = SetupFrame(content_frame, None)
    content_frame.pack()
    window.mainloop()
