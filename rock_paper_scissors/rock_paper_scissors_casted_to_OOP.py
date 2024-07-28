from random import randint
from ascii_art import logo, rps_ascii

class RockPaperScissors:
    def __init__(self):
        self.machine_input = None
        self.user_input = None
        print(logo)

    def get_machine_input(self):
        self.machine_input = randint(0, 2)

    def get_user_input(self):
        while True:
            user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ").strip()
            if user_input in ['0', '1', '2']:
                break
            elif not user_input:
                print(f"You typed 'Null'. Game ended.")
                return False
            else:
                print(f"You typed '{user_input}'. Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
        return True

    def determine_winner(self):
        if self.user_input == 0 and self.machine_input == 1:
            return f"Game Over!\nMachine wins with {rps_ascii[1]} \nyou {rps_ascii[0]}."
        elif self.user_input == 1 and self.machine_input == 2:
            return f"Game Over!\nMachine wins with {rps_ascii[2]} \nyou {rps_ascii[1]}."
        elif self.user_input == 2 and self.machine_input == 0:
            return f"Game Over!\nMachine wins with {rps_ascii[0]} \nyou {rps_ascii[2]}."
        elif self.machine_input == self.user_input:
            return f"DRAW!\nMachine {rps_ascii[self.machine_input]}\nyou {rps_ascii[self.user_input]}."
        else:
            return f"Machine {rps_ascii[self.machine_input]}\nYou win!\nYou {rps_ascii[self.user_input]}."

    def play(self):
        while True:
            self.get_machine_input()
            if not self.get_user_input():
                break
            result = self.determine_winner()
            print(result)

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()