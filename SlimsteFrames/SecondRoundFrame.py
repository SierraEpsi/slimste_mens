import tkinter as tk


class SecondRoundFrame:
    def __init__(self, frame, answers):
        # Set up frame structure
        self.answers = answers
        self.info_frame = tk.Frame(master=frame, bg="grey", pady=5, padx=5)
        self.info_frame.pack(side="top", fill="x")
        self.refresh_frame()

    def refresh_frame(self):
        for widget in self.info_frame.winfo_children():
            widget.destroy()

        for i, answer in enumerate(self.answers):
            color="red"
            if answer["given"]:
                color = "white"
            label = tk.Label(
                master=self.info_frame,
                text=answer["answer"],
                font=("Arial", 16, "bold"),
                fg=color,
                bg="red",
                padx=10,
                pady=5,
            )
            label.grid(row=i, column=0, padx=5, pady=5)

    def reveal_answer(self, answer_nb):
        self.answers[answer_nb]["given"] = True
        self.refresh_frame()

if __name__ == "__main__":
    window = tk.Tk()
    content_frame = tk.Frame(window)
    these_answers = [
            {"answer": "test1", "given":False},
            {"answer": "test2", "given":True},
            {"answer": "test3", "given":False},
            {"answer": "test4", "given":False},
        ]
    first_round_frame = SecondRoundFrame(content_frame, these_answers)
    content_frame.pack()
    window.mainloop()
