from ..data.beep import beeps
class Letter:
    def __init__(self, letter, morse):
        self.letter = letter
        self.morse = morse
        
    def morse_output(self):
        print(self.letter)
        for char in self.morse:
            beeps[char]()
        beeps[' ']()