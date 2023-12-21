class Player:
    def __init__(self, name):
        self.name = name
        self.is_playing = False
        self.score = 60
        self.answered = False
        self.played = False
        
    def get_score(self):
        return self.score
    
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
        
    def answer(self):
        self.answered = True
        self.is_playing = True
        
    def pass_question(self):
        self.is_playing = False
