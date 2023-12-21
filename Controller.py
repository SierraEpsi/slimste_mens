from SlimsteUtils.Answers import Answers
from SlimsteUtils.Player import Player


class Controller:
    def __init__(self, content_window):
        self.players = []
        self.current_player = 0
        self.content_window = content_window
        self.questions_1 = None
        self.round_nb = 0
        self.question_nb = 0
        self.playing = False
        self.wrong_answers = 0
        self.NB_ROUND_1 = 15
        self.current_answers = None
        self.answers = Answers()

    def get_current_round(self):
        return self.round_nb

    def get_current_question(self):
        return self.question_nb

    def get_current_player(self):
        return self.current_player

    def get_wrongs_answers(self):
        return self.wrong_answers

    def get_current_answers(self):
        return self.current_answers

    def is_playing(self):
        return self.playing

    def update_candidates(self):
        print("UPDATING SPELERS: ", self.players, self.current_player)
        if self.current_player == -1:
            self.content_window.get_candidate_frame().update_candidates(self.players, -1)
        else:
            self.content_window.get_candidate_frame().update_candidates(self.players, self.current_player)

    def add_candidates(self, player_names):
        for player_name in player_names:
            self.players.append(Player(player_name))
        self.update_candidates()

    def start_round_1(self):
        self.round_nb = 1
        self.question_nb = 1
        self.playing = True
        self.content_window.create_round_1()

    def next_candidate_1(self):
        self.current_player += 1
        if self.current_player > 2:
            self.current_player = 0
        print("VOLGENDE SPELER: ", self.current_player)
        self.content_window.get_candidate_frame().update_candidates(self.players, self.current_player)

    def correct_answer_1(self):
        if self.playing:
            print("CORRECT")
            self.playing = False
            if self.question_nb % 3 == 0:
                self.players[self.current_player].add_score(10)
                self.update_candidates()

    def wrong_answer_1(self):
        if self.playing:
            self.wrong_answers += 1
            if self.wrong_answers > 2:
                self.playing = False
                print("FOUT, STOP VRAAG")
            else:
                print("FOUT")
            self.next_candidate_1()

    def next_question_1(self):
        self.playing = True
        self.wrong_answers = 0
        self.question_nb += 1
        if self.question_nb > self.NB_ROUND_1:
            print("VRAGEN ZIJN OP")
        else:
            print("VOLGENDE VRAAG")
            self.content_window.get_content_frame().refresh_frame(self.question_nb)
        self.update_candidates()

    def start_round_2(self):
        self.round_nb = 2
        self.question_nb = 1
        self.playing = False
        self.current_answers = [{"answer": answer, "given": False} for answer in self.answers.get_asnwers(self.round_nb, self.question_nb)]
        self.content_window.create_round_2(self.current_answers)
        for player in self.players:
            player.new_round()
        self.current_player = self.next_candidate_to_play()
        self.update_candidates()

    def next_candidate_to_play(self):
        lowest_score = 999
        for player in self.players:
            if not player.has_played():
                lowest_score = min(lowest_score, player.get_score())
        for i, player in enumerate(self.players):
            if not player.has_played() and lowest_score == player.get_score():
                return i
        return -1

    def next_candidate_to_answer(self):
        lowest_score = 999
        for player in self.players:
            if not player.has_answered():
                lowest_score = min(lowest_score, player.get_score())
        for i, player in enumerate(self.players):
            if not player.has_answered() and lowest_score == player.get_score():
                return i
        return -1

    def have_all_players_played(self):
        for player in self.players:
            if not player.has_played():
                return False
        return True

    def have_all_players_answered(self):
        for player in self.players:
            if not player.has_answered():
                return False
        return True

    def reveal_answer_2(self, answer_nb):
        if not self.current_answers[answer_nb]["given"]:
            self.current_answers[answer_nb]["given"] = True
            self.content_window.get_content_frame().reveal_answer(answer_nb)
            if self.playing:
                self.players[self.current_player].add_score(20)
                self.update_candidates()

    def start_question_2(self):
        if not self.playing:
            print("PLAYER START PLAYING")
            self.playing = True
            self.players[self.current_player].play()

    def continue_question_2(self):
        if not self.playing:
            print("PLAYER CONTINUE PLAYING")
            self.playing = True
            self.players[self.current_player].answer()

    def pass_question_2(self):
        if self.playing:
            print("PLAYER PASSES")
            self.playing = False
            self.players[self.current_player].pass_question()
            self.current_player = self.next_candidate_to_answer()
            self.update_candidates()

    def next_question_2(self):
        if self.question_nb < 3:
            self.question_nb += 1
            self.playing = False
            self.current_answers = [{"answer": answer, "given": False} for answer in self.answers.get_asnwers(self.round_nb, self.question_nb)]
            self.content_window.create_round_2(self.current_answers)
            for player in self.players:
                player.new_question()
            self.current_player = self.next_candidate_to_play()
            self.update_candidates()
