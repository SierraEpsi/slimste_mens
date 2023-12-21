from SlimsteUtils.Questions import Questions
from SlimsteUtils.Player import Player


class Controller:
    def __init__(self, content_window, control_window):
        self.content_window = content_window
        self.control_window = control_window
        self.players = []
        self.current_player = 0
        self.content_window = content_window
        self.questions_1 = None
        self.round_nb = 0
        self.question_nb = 0
        self.game_state = ""
        self.wrong_answers = 0
        self.NB_ROUND_1 = 15
        self.current_question = None
        self.questions = Questions()

    def get_current_round(self):
        return self.round_nb

    def get_current_question_nb(self):
        return self.question_nb

    def get_current_player(self):
        return self.current_player

    def get_wrongs_answers(self):
        return self.wrong_answers

    def get_current_question(self):
        return self.current_question

    def add_candidates(self, player_names):
        for player_name in player_names:
            self.players.append(Player(player_name))
        self.content_window.init_candidates(self.players)
        self.content_window.refresh(self.players)

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

    def refresh(self):
        if self.round_nb == 1:
            self.content_window.refresh(self.players, current_player=self.current_player, question_nb=self.question_nb)
        else:
            self.content_window.refresh(self.players, current_player=self.current_player)
        self.control_window.refresh(self.game_state)

    def start_round_1(self):
        self.round_nb = 1
        self.question_nb = 1
        self.current_player = 0
        self.game_state = "PLAY"
        self.content_window.create_round_1()
        self.refresh()

    def next_candidate_1(self):
        self.current_player += 1
        if self.current_player > 2:
            self.current_player = 0
        print("VOLGENDE SPELER: ", self.current_player)
        self.refresh()

    def correct_answer_1(self):
        if self.game_state == "PLAY":
            print("CORRECT")
            self.game_state = "END"
            if self.question_nb % 3 == 0:
                self.players[self.current_player].add_score(10)
            self.refresh()

    def wrong_answer_1(self):
        if self.game_state == "PLAY":
            self.wrong_answers += 1
            if self.wrong_answers > 2:
                self.game_state = "END"
                print("FOUT, STOP VRAAG")
            else:
                print("FOUT")
            self.next_candidate_1()

    def next_question_1(self):
        self.game_state = "PLAY"
        self.wrong_answers = 0
        self.question_nb += 1
        if self.question_nb > self.NB_ROUND_1:
            print("VRAGEN ZIJN OP")
        else:
            print("VOLGENDE VRAAG")
        self.refresh()

    def reveal_answer(self, answer_nb):
        if not self.current_question.get_answer(answer_nb).is_revealed():
            self.current_question.get_answer(answer_nb).reveal()
            if self.game_state == "PLAY":
                self.players[self.current_player].add_score(20)
            if self.current_question.is_answered():
                self.game_state = "END"
            self.refresh()

    def start_question(self):
        print("PLAYER START PLAYING")
        self.game_state = "PLAY"
        self.players[self.current_player].play()
        self.control_window.refresh(self.game_state)

    def continue_question(self):
        print("PLAYER CONTINUE PLAYING")
        self.game_state = "PLAY"
        self.players[self.current_player].answer()
        self.refresh()

    def pass_question(self):
        print("PLAYER PASSES")
        self.players[self.current_player].pass_question()
        if self.have_all_players_answered():
            self.game_state = "END"
            self.current_question.reveal()
        else:
            self.game_state = "PAUSE"
            self.current_player = self.next_candidate_to_answer()
        self.refresh()

    def next_question(self):
        if self.question_nb < 3:
            self.question_nb += 1
            self.game_state = "START"
            self.current_question = self.questions.get_question(self.round_nb, self.question_nb)
            if self.round_nb == 2:
                self.content_window.create_round_2(self.current_question)
            elif self.round_nb == 3:
                self.content_window.create_round_3(self.current_question)
            for player in self.players:
                player.new_question()
            self.current_player = self.next_candidate_to_play()
            self.refresh()

    def start_round_2(self):
        self.round_nb = 2
        self.question_nb = 1
        self.game_state = "START"
        self.current_question = self.questions.get_question(self.round_nb, self.question_nb)
        self.content_window.create_round_2(self.current_question)
        for player in self.players:
            player.new_round()
        self.current_player = self.next_candidate_to_play()

    def start_round_3(self):
        self.round_nb = 3
        self.question_nb = 1
        self.game_state = "START"
        self.current_question = self.questions.get_question(self.round_nb, self.question_nb)
        self.content_window.create_round_3(self.current_question)
        for player in self.players:
            player.new_round()
        self.current_player = self.next_candidate_to_play()
