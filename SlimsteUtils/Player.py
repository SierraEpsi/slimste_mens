import time


class Player:
    def __init__(self, name):
        self.name = name
        self.is_playing = False
        self.score = 60
        self.answered = False
        self.played = False
        self.start_time = None
        
    def get_score(self):
        if not self.is_playing:
            return self.score
        current_score = self.score
        current_time = time.time()
        elapsed_time = int(current_time - self.start_time)
        current_score -= elapsed_time
        return current_score
    
    def get_name(self):
        return self.name
    
    def has_played(self):
        return self.played
    
    def has_answered(self):
        return self.answered
        
    def new_round(self):
        self.played = False
        self.answered = False
        
    def new_question(self):
        self.answered = False
        
    def add_score(self, amount):
        self.score += amount
        
    def play(self):
        self.played = True
        self.answered = True
        self.is_playing = True
        self.start_time = time.time()
        
    def answer(self):
        self.answered = True
        self.is_playing = True
        self.start_time = time.time()
        
    def pass_question(self):
        self.is_playing = False
        stop_time = time.time()
        elapsed_time = int(stop_time - self.start_time)
        self.score -= elapsed_time
