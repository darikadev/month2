import random
class Game:
    def __init__ (self):
        self.words = ["PINEAPPLE","LEMON","WATERMELON","RESTBERRY"]
        self.chances = 7
        self.result = ""
    def introduction (self):
        print("Welcome to our Golden Game!!")
        print(f"You have {self.chances} chances to ein this game!")
        print("You need to text letters to guess the out word.")
        print("GOOD LUCK!")

    def select_word(self):
        self.result= random.choice(self.words)
    def start (self):
        guessed_letters = []
        while self.chances > 0:
            letter = input("Please enter a Letter:").upper()
            if letter in self.result:
                guessed_letters.append(letter)
                print("Congratulations!You guessed a Letter!")
            else:
                print("Incorrect guess.Try again !")
                self.chances-=1
        displayed_word = ""
        for letter_in_word in self.result:
            if letter_in_word in guessed_letters:
                displayed_word +=""
            print(f"Congratulations! You won!The word was {self.result} ")
            break
        if self.chances == 0:
         print(f"GAME OVER!You lost the Game. The word was{self.result}")
game= Game()
game.introduction()
game.select_word()
game.start()