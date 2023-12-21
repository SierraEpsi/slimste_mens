class Answer:
    def __init__(self, answer):
        self.answer = answer
        self.revealed = False

    def get_answer(self):
        return self.answer

    def is_revealed(self):
        return self.revealed

    def reveal(self):
        self.revealed = True


class Hint:
    def __init__(self, hint, color):
        self.hint = hint
        self.color = color
        self.revealed = False

    def get_hint(self):
        return self.hint

    def get_color(self):
        return self.color

    def is_revealed(self):
        return self.revealed

    def reveal(self):
        self.revealed = True


class SecondRoundQuestion:
    def __init__(self, question, answers):
        self.question = question
        self.answers = [Answer(answer) for answer in answers]

    def get_question(self):
        return self.question

    def get_answers(self):
        return self.answers

    def get_answer(self, answer_nb):
        return self.answers[answer_nb]

    def reveal_answer(self, answer_nb):
        self.answers[answer_nb].reveal()

    def reveal(self):
        for answer in self.answers:
            answer.reveal()

    def is_answered(self):
        for answer in self.answers:
            if not answer.is_revealed():
                return False
        return True


class ThirdRoundAnswer(Answer):
    def __init__(self, answer, hints, color):
        Answer.__init__(self, answer)
        self.hints = [Hint(hint, color) for hint in hints]
        self.color = color

    def get_hints(self):
        return self.hints

    def get_color(self):
        return self.color

    def reveal(self):
        Answer.reveal(self)
        for hint in self.hints:
            hint.reveal()


class ThirdRoundQuestion:
    def __init__(self, answers):
        self.answers = answers

    def get_answers(self):
        return self.answers

    def get_answer(self, answer_nb):
        return self.answers[answer_nb]

    def reveal_answer(self, answer_nb):
        self.answers[answer_nb].reveal()

    def reveal(self):
        for answer in self.answers:
            answer.reveal()

    def is_answered(self):
        for answer in self.answers:
            if not answer.is_revealed():
                return False
        return True


class Questions:
    def __init__(self):
        self.round_2_answers = [
            SecondRoundQuestion("Q1?", ("Q1_A1", "Q1_A2", "Q1_A3", "Q1_A4")),
            SecondRoundQuestion("Q2?", ("Q2_A1", "Q2_A2", "Q2_A3", "Q2_A4")),
            SecondRoundQuestion("Q3?", ("Q3_A1", "Q3_A2", "Q3_A3", "Q3_A4"))
        ]

        self.round_3_answers = [
            ThirdRoundQuestion((
                ThirdRoundAnswer("P1_A1", ("P1_A1_H1", "P1_A1_H2", "P1_A1_H3", "P1_A1_H4"), "blue"),
                ThirdRoundAnswer("P1_A2", ("P1_A2_H1", "P1_A2_H2", "P1_A2_H3", "P1_A2_H4"), "green"),
                ThirdRoundAnswer("P1_A3", ("P1_A3_H1", "P1_A3_H2", "P1_A3_H3", "P1_A3_H4"), "orange"),
            )),ThirdRoundQuestion((
                ThirdRoundAnswer("P2_A1", ("P2_A1_H1", "P2_A1_H2", "P2_A1_H3", "P2_A1_H4"), "blue"),
                ThirdRoundAnswer("P2_A2", ("P2_A2_H1", "P2_A2_H2", "P2_A2_H3", "P2_A2_H4"), "green"),
                ThirdRoundAnswer("P2_A3", ("P2_A3_H1", "P2_A3_H2", "P2_A3_H3", "P2_A3_H4"), "orange"),
            )),ThirdRoundQuestion((
                ThirdRoundAnswer("P3_A1", ("P3_A1_H1", "P3_A1_H2", "P3_A1_H3", "P3_A1_H4"), "blue"),
                ThirdRoundAnswer("P3_A2", ("P3_A2_H1", "P3_A2_H2", "P3_A2_H3", "P3_A2_H4"), "green"),
                ThirdRoundAnswer("P3_A3", ("P3_A3_H1", "P3_A3_H2", "P3_A3_H3", "P3_A3_H4"), "orange"),
            ))
        ]

    def get_question(self, round_nb, question_nb):
        question_nb -= 1
        if round_nb == 2:
            return self.round_2_answers[question_nb]
        if round_nb == 3:
            return self.round_3_answers[question_nb]
        return -1


if __name__ == "__main__":
    questions = Questions()
    print(questions.get_questions(3,1))
