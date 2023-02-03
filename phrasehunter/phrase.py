


class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.hidden_phrase = ['_' if char != ' ' else ' ' for char in phrase]

        self.guessed_letters = []

    def display(self):
        return ' '.join(self.hidden_phrase)

    def check_letter(self, letter):
        if letter in self.guessed_letters or letter == ' ':
            return False
        self.guessed_letters.append(letter)
        if letter in self.phrase:
            for i in range(len(self.phrase)):
                if self.phrase[i] == letter:
                    self.hidden_phrase[i] = letter
            return True
        else:
            self.guessed_letters.append(letter)
            return False


