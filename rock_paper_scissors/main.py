## Project: Rock - Paper - Scissors.
from random import randint
from ascii_art import logo, rps_ascii
print(logo)

while not False:
    machine_input = randint(0, 2)
    user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ").strip()
    if user_input not in '012':
        print(f"You typed '{user_input}'. Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
    elif not user_input:
        print(f"You typed 'Null'. Game ended.")
        break
    else:
        user_input = int(user_input)

        if user_input == 0 and machine_input == 1:
            print(f"Game Over!\nMachine win with {rps_ascii[1]} \nyou {rps_ascii[0]}.")
        elif user_input == 1 and machine_input == 2:
            print(f"Game Over!\nMachine win with {rps_ascii[2]} \nyou {rps_ascii[1]}.")
        elif user_input == 2 and machine_input == 0:
            print(f"Game Over!\nMachine win with {rps_ascii[0]} \nyou {rps_ascii[2]}.")
        elif machine_input == user_input:
            print(f"DRAW!\nMachine  {rps_ascii[machine_input]}\nyou {rps_ascii[user_input]}.")
        else:
            print(f"Machine {rps_ascii[machine_input]}\nYou win!\nYou {rps_ascii[user_input]} ")