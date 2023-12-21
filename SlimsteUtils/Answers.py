class Answers:
    def __init__(self):
        self.round_2_answers = [
            ["Q1_A1", "Q1_A2", "Q1_A3", "Q1_A4"],
            ["Q2_A1", "Q2_A2", "Q2_A3", "Q2_A4"],
            ["Q3_A1", "Q3_A2", "Q3_A3", "Q3_A4"]
        ]
        self.round_3_words = [
            ["Q1_A1", "Q1_A2", "Q1_A3", "Q1_A4"],
            ["Q2_A1", "Q2_A2", "Q2_A3", "Q2_A4"],
            ["Q3_A1", "Q3_A2", "Q3_A3", "Q3_A4"]
        ]

    def get_asnwers(self, round_nb, question_nb):
        question_nb -= 1
        if round_nb == 2:
            return self.round_2_answers[question_nb]
        return -1
