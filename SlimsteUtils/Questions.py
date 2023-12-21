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


class FourthRoundQuestion:
    def __init__(self, answers):
        self.answers = [Answer(answer) for answer in answers]

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


class FifthRoundQuestion:
    def __init__(self, answers):
        self.answers = [Answer(answer) for answer in answers]

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

class FinalRoundQuestion:
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

class Questions:
    def __init__(self):
        self.round_2_questions = [
            SecondRoundQuestion("Comment fait-t-on du Guacamole selon Jeroen Meus? (je te donnes déjà les avocats)",
                                ("Poivre et sel",
                                 "Coriandre",
                                 "Citron vert",
                                 "Aille")),
            SecondRoundQuestion("Quelles sont les show Broadway les plus joués?",
                                ("Phantom of the Opera",
                                 "Chicago",
                                 "The Lion King",
                                 "Wicked")),
            SecondRoundQuestion("Tintin, Lucky Luke, Peanuts et Asterix sont mes heros preferes, mais connais tu leurs chiens?",
                                ("Milou",
                                 "Rataplan",
                                 "Snoopy",
                                 "Idefix"))
        ]

        self.round_3_questions = [
            ThirdRoundQuestion((
                ThirdRoundAnswer("Mop",
                                 ("VAAK OVER DOMME BLONDJES",
                                  "OOK EEN ZWABBER",
                                  "EINDIGT MET EEN POINTE",
                                  "DIE VAN DE DUIZEND DRUPPELS"), "blue"),
                ThirdRoundAnswer("Max",
                                 ("AFKORTING VAN MAXIMUM",
                                  "ANTICLI…",
                                  "NIKE AIR …",
                                  "PEPSI …"), "green"),
                ThirdRoundAnswer("Mum",
                                 ("…BAI",
                                  "ENGELS VOOR MAMA",
                                  "IN EEN … VAN TIJD",
                                  "MINI..."), "orange"),
            )),ThirdRoundQuestion((
                ThirdRoundAnswer("Zwager",
                                 ("ZEGGEN ZE VOORAL IN NEDERLAND",
                                  "NIET SLAGER",
                                  "NIET ZWANGER",
                                  "SYNONIEM VOOR SCHOONBROER"), "blue"),
                ThirdRoundAnswer("Gaatjes",
                                 ("BETER NIET IN JE TANDEN",
                                  "IN JE OREN",
                                  "KAAS HEEFT HET SOMS",
                                  "PRAATJES VULLEN GEEN ..."), "green"),
                ThirdRoundAnswer("Brusselse Cafées",
                                 ("HET GOUDBLOMMEKKE IN PAPIER",
                                  "L'ARCHIDUC",
                                  "POECHENELLE-KELDER",
                                  "MONK"), "orange"),
            )),ThirdRoundQuestion((
                ThirdRoundAnswer("Dad jokes",
                                 ("FLAUWE MOPPEN",
                                  "HEEL VOORSPELBAAR",
                                  "JE VADER MAAKT ZE",
                                  "VAAK EEN WOORDSPELING"), "blue"),
                ThirdRoundAnswer("Pond",
                                 ("80 EUROCENT",
                                  "ONGEVEER 500 GRAM",
                                  "OOK ENGELSE VIJVER",
                                  "TIEN ... GRUTTEN"), "green"),
                ThirdRoundAnswer("Doe een duck-face!",
                                 ("ALSOF JE POSEERT VOOR EEN FOTO",
                                  "DOE HET MAAR!",
                                  "ZOALS EEN EEND",
                                  "MET GETUITEN LIPPEN"), "orange"),
            ))
        ]

        self.round_4_questions = [
            FourthRoundQuestion(("Jack Sparrow",
                                 "Neo",
                                 "Tylar Durden",
                                 "Agent Jay",
                                 "Terminator",
                                 "Tony Stark",
                                 "Harry Potter",
                                 "Jack",
                                 "Gandalf",
                                 "Shrek")),
            FourthRoundQuestion(("Horny",
                                 "You don't know me",
                                 "Alors on danse",
                                 "Champs Elysees",
                                 "Tainted love",
                                 "Eternal flame",
                                 "Carol of the bells",
                                 "Blue",
                                 "Yeah",
                                 "Circle of life")),
            FourthRoundQuestion(("Cantillon",
                                 "Pantalon",
                                 "Triathlon",
                                 "Cochon",
                                 "Carillon",
                                 "Parthenon",
                                 "Cupidon",
                                 "Bouchon",
                                 "Zillion",
                                 "Non"))
        ]

        self.round_5_questions = [
            FifthRoundQuestion(("Apollo-11",
                                "Neil Armstrong",
                                "Buzz Aldrin",
                                "Michael Collins",
                                "1969")),
            FifthRoundQuestion(("Oscar",
                                "Forrest Gump",
                                "Tom Hanks",
                                "Robin Wright",
                                "John F. Kennedy")),
            FifthRoundQuestion(("Val Cenis",
                                "Anvers Amitie",
                                "Haute-Maurienne Vanoise",
                                "Philippe Roger",
                                "France"))
        ]

        self.round_final_questions = [
            FinalRoundQuestion("Wat zijn de vijf grootste steden aan de E19?",
                ("Antwerpen",
                "Mechelen",
                "Brussel",
                "Nijvel",
                "Bergen")),
            FinalRoundQuestion("Wat zijn de bekendste vulkanen in Europa?",
                ("Etna",
                "Vesuvius",
                "Stromboli",
                "Katla",
                "Eyjefjallajökull")),
            FinalRoundQuestion("Met welke toestellen wordt het weer gemeten?",
                ("Thermometer",
                "Barometer",
                "Anemometer",
                "Pluviometer",
                "Windzak")),
            FinalRoundQuestion("Met welke toestellen wordt het weer gemeten?",
                ("Thermometer",
                "Barometer",
                "Anemometer",
                "Pluviometer",
                "Windzak")),
            FinalRoundQuestion("Wie is Marion Jones?",
                ("Amerikaanse",
                "Verspringen",
                "Sprinten",
                "Doping",
                "Tim Montgomery")),
            FinalRoundQuestion("Wat zijn de meest verkochte merken toiletpapier bij Delhaize?",
                ("Edet",
                "Page",
                "Lotus",
                "Scottex",
                "Moltonel")),
            FinalRoundQuestion("Wat weet je over mevrouw Beloy?",
                ("Tatyana",
                "Actrice",
                "Presentatrice",
                "Adriaan Van den Hoof",
                "Vlaanderen Vakantieland")),
            FinalRoundQuestion("In welke vijf landen liggen de meeste IKEA-vestigingen?",
                ("Duitsland",
                "Verenigde Staten",
                "Frankrijk",
                "Italië",
                "Verenigd Koningrijk")),
            FinalRoundQuestion("Wat weet je over Urbanus?",
                ("Urbain Servranckx",
                "Tollembeek",
                "Van Anus",
                "Koko Flanel",
                "Stripreeks")),
            FinalRoundQuestion("Wat weet je over Machu Picchu?",
                ("Inca’s",
                "Peru",
                "Werelderfgoed",
                "Stad",
                "Bergen")),
            FinalRoundQuestion("Wat heb je behalve gehakt en tomatensaus nog nodig om spaghetti te maken?",
                ("Wortel",
                "Ui",
                "Paprika",
                "Champignons",
                "Courgettes")),
            FinalRoundQuestion("Wat weet je over Koning Arthur?",
                ("Merlijn",
                "Lancelot",
                "Excalibur",
                "Camelot",
                "Ronde Tafel")),
            FinalRoundQuestion("Wie was Pol Pot?",
                ("Cambodja",
                "Rode Khmer",
                "Dictator",
                "Communist",
                "Killing Fields")),
            FinalRoundQuestion("Van welk vijf Vlaamse gemeenten begint de naam met ‘La’?",
                ("Laakdal",
                "Laarne",
                "Lanaken",
                "Landen",
                "Langemark-Poelkapelle")),
            FinalRoundQuestion("De vijf belangrijkste basisingrediënten van Jupiler?",
                ("Mout",
                "Water",
                "Gist",
                "Hop",
                "Maïs")),
            FinalRoundQuestion("Noem de 5 Kardashian/Jenner dochters",
                ("Kourtney",
                "Kim",
                "Khloé",
                "Kendall",
                "Kylie")),
            FinalRoundQuestion("Welke landen zijn naast de Verenigde Staten en het Verenigd Koninkrijk nog lid van de G7?",
                ("Frankrijk",
                "Duitsland",
                "Italië",
                "Japan",
                "Canada")),
            FinalRoundQuestion("Flair vroeg aan vrouwen waar ze op seksueel vlak niet mee willen experimenteren. Wat is top vijf?",
                ("Parenclub",
                "SM",
                "Webcamseks",
                "Triootje",
                "Anale seks")),
            FinalRoundQuestion("Wat zijn de vijf grootste delers van het getal 18? Bij een fout eindigt je beurt!",
                ("18",
                "9",
                "6",
                "3",
                "2")),
            FinalRoundQuestion("Wat weet je over de film ‘American Beauty’?",
                ("rozensoort",
                "Sam Mendes",
                "Kevin Spacey",
                "midlifecrisis",
                "oscar")),
            FinalRoundQuestion("Wat weet je over Sam de Bruyn?",
                ("Studio brussel",
                "Gent",
                "Presentator",
                "Getrouwd",
                "Voor de mannen")),
            FinalRoundQuestion("Wat weet je over Game of thrones?",
                ("Amerikaanse",
                "Televisiereeks",
                "HBO",
                "George R.R. Martin",
                "Fantasy")),
            FinalRoundQuestion("Hoe maak je wentelteefjes klaar?",
                ("Brood",
                "Melk",
                "Eieren",
                "Weken",
                "Bakken")),
            FinalRoundQuestion("Zuid Soedan en Zambia krijg je al. De namen van welke andere staten beginnen met de letter ‘Z’?",
                ("Zwitserland",
                "Zweden",
                "Zuid-Afrika",
                "Zuid-Korea",
                "Zimbabwe")),
            FinalRoundQuestion("Wat weet je over Maria Sharapova?",
                ("Russische",
                "Tennis",
                "Babe",
                "Wimbledon",
                "Kreunt")),
            FinalRoundQuestion("Het is een Rus, dat is zeker, maar wat weet je nog meer over Michail Gorbatsjov?",
                ("Wijnvlek",
                "President",
                "Glasnost",
                "Perestrojka",
                "Nobelprijs Vrede"))
        ]

    def get_question(self, round_nb, question_nb):
        question_nb -= 1
        if round_nb == 2:
            return self.round_2_questions[question_nb]
        if round_nb == 3:
            return self.round_3_questions[question_nb]
        if round_nb == 4:
            return self.round_4_questions[question_nb]
        if round_nb == 5:
            return self.round_5_questions[question_nb]
        if round_nb == 6:
            return self.round_final_questions[question_nb]
        return -1


if __name__ == "__main__":
    questions = Questions()
    print(questions.get_questions(3,1))
