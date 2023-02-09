import random
from .phrase import Phrase




class Game:
    def __init__(self):
        self.phrases = [
               Phrase("A bird in the hand is worth two in the bush"),
               Phrase("Actions speak louder than words"),
               Phrase("All is fair in love and war"),
               Phrase("Every cloud has a silver lining"),
               Phrase("Early bird catches the worm"),
               Phrase("The proof of the pudding is in the eating")]
        self.active_phrase = None
        self.missed = 0
        self.guesses = []

    def get_random_phrase(self):
         self.active_phrase = random.choice(self.phrases)
        
    def start(self):
        print("Welcome to Phrasehunter! Can you guess the Phrase!")
        self.get_random_phrase()
        while not self.game_over():
            current_phrase = self.active_phrase.display()
            print(f"Current phrase: {current_phrase}")
            letter = input("Guess a letter: ").lower()
            correct = self.guess(letter)
            if not correct:
                self.missed += 1
                self.guesses.append(letter)
                print(f"Wrong gueses: {','.join(self.guesses)}")
                print(f"Incorrect! You have {5 - self.missed} guesses left.")

        if '_' not in self.active_phrase.display():
            print(f"Congratulations! You won the game. The phrase was: {self.active_phrase.phrase}")
        else:
            print(f"You lost the game. The phrase was: {self.active_phrase.phrase}")

    def game_over(self):
        return '_' not in self.active_phrase.display() or self.missed >= 5

    def guess(self, letter):
        correct = self.active_phrase.check_letter(letter)
        return correct
