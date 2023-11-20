import random

class Quiz:
    def _init_(self):
        self.questions = []
        self.answers = []
        self.score = 0
        self.highscore = 0

    def add_question(self, question, answer):
        self.questions.append(question)
        self.answers.append(answer)

    def display_question(self):
        index = random.randint(0, len(self.questions) - 1)
        return self.questions[index]

    def check_answer(self, user_answer, correct_answer):
        return user_answer.lower() == correct_answer.lower()

    def play(self):
        print("Willkommen beim Quiz!")
        print("Beantworte die folgenden Fragen:")
        while True:
            question = self.display_question()
            print("\nFrage:", question)
            user_answer = input("Antwort: ")
            
            if self.check_answer(user_answer, self.answers[self.questions.index(question)]):
                print("Richtig!")
                self.score += 1
            else:
                print("Falsch. Die richtige Antwort ist:", self.answers[self.questions.index(question)])
            
            print("Aktueller Punktestand:", self.score)
            
            play_again = input("Möchtest du weiterspielen? (ja/nein): ")
            if play_again.lower() != 'ja':
                print("Spiel beendet. Dein Endpunktestand:", self.score)
                
                if self.score > self.highscore:
                    self.highscore = self.score
                    print("Herzlichen Glückwunsch! Du hast einen neuen Highscore erreicht:", self.highscore)
                
                break

                

quiz = Quiz()
quiz.add_question("Was ist die Hauptstadt von Frankreich?", "Paris")
quiz.add_question("Was ist die Hauptstadt von Deutschland?", "Berlin")
quiz.add_question("Was ist die Hauptstadt von Spanien?", "Madrid")
quiz.add_question("Was ist die Hauptstadt von Schweden?", "Stockholm")
quiz.add_question("Wieviele Monate hat das Jahr?", "12")
quiz.add_question("Wieviele Bundesländer hat Deutschland?", "16")
quiz.add_question("Wie heißt unsere Uni?", "Leuphana")
quiz.add_question("Mit welcher KI hab ich diesen Code generiert?", "ChatGPT")
quiz.add_question("Was heißt Liebe auf französisch?", "amour")
quiz.add_question("Wie heißt der Datentyp für eine Zeichenkette?", "String")
quiz.add_question("Was ist die meist verwendete Funktion in Python?", "print")
quiz.add_question("Wer hat den Begriff der Falsifikation geprägt?", "Karl Popper")
quiz.add_question("Welche Note ist eine Terz zur Note C?", "E")
quiz.add_question("Wie geht die C-Dur Tonleiter, schreibe sie in der richtigen reihenfolge  ohne Leerzeichen von c bis c auf?", "cdefgahc")
quiz.add_question("Was ist ein muss auf dem Weihnachtsmarkt? a: Glühwürmchen b: Gummistiefel c: Gebrannte Mandeln oder d: Schmalzlocken. Wähle eine Antwort aus und schreibe nur den Buchstaben", "c")
quiz.add_question("Was heißt das erste Rentier in dem Lied, Rudolf the red nose reindeer?", "Dasher")
quiz.add_question("Welche Farbe kommt raus wenn man rot und blau mischt?", "lila")
quiz.add_question("Wie heißt die bekannte Sehenswürdigkeit in Paris? a: der schiefe Turm von Paris b: die Freiheitsstatur in Dubai c: das Tor de France oder d: la Tour Eiffel. Wähle eine Antwort aus und schreibe nur den Buchstaben ", "d")
quiz.add_question("Wie findest du dieses Quiz? a: richtig beschissen b: niederträchtig c: supergalaktisch einzigartig wundertoll oder d: bodenlos unterste Schublade. Wähle eine Antwort aus und schreibe nur den Buchstaben ", "c")




quiz.play()
