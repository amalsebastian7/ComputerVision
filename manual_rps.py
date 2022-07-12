import random
class Game:

    def __init__(self,input_value):
        self.input_value=['Rock','Paper','Scissors']

    def get_computer_choice(self) :
        self.computer_choice = random.choice(self.input_value)
        return self.computer_choice
    
    
    def get_human_choice(self):    
        self.human_choice = input("Please enter your choice: Rock/Paper/Scissors?   ")
        print(f"The user chose: {self.human_choice}")
        print(f"The computer chose: {self.computer_choice}")
        pass
    
    def get_winner(self) :
        if self.human_choice == self.computer_choice:
            print("It's a tie!")
        elif self.human_choice == 'Rock':
            if self.computer_choice == 'Paper':
                print("The computer wins!")
            else:
                print("You win!")
        elif self.human_choice == 'Paper':
            if self.computer_choice == 'Scissors':
                print("The computer wins!")
            else:
                print("You win!")
        elif self.human_choice == 'Scissors':
            if self.computer_choice == 'Rock':
                print("The computer wins!")
            else:
                print("You win!")
        pass
    def play(self):
        self.get_computer_choice()
        self.get_human_choice()
        self.get_winner()

rps=Game(['Rock','Paper','Scissors'])
rps.play()
