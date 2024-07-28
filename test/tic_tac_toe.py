player_1 = []
player_2 = []
# win_1 = 1 and 2 and 3
win_1, win_2, win_3, win_4, win_5, win_6, win_7 = [1, 2, 3], [1, 4, 7], [7, 8, 9], [3, 6, 9], [4, 5, 6], [1, 5, 9], [3, 5, 7]
set1, set2, set3, set4, set5, set6, set7 = set(win_1), set(win_2), set(win_3), set(win_4), set(win_5), set(win_6), set(win_7)

while True:
    player_1_input = int(input("Player 1 board location: "))
    player_1.append(player_1_input)
    set1_p1 = set(player_1)
    if player_1_input == '':
        break
    if set1_p1 == set1 or set1_p1 == set2 or set1_p1 == set3 or set1_p1 == set4 or set1_p1 == set5 or set1_p1 == set6 or set1_p1 == set7:
        print("Player 1 won the game.")
        should_continue = input("Play again? 'y' or 'n': ")
        if should_continue == 'y':
            continue

    player_2_input = int(input("Player 2 board location: "))
    player_2.append(player_2_input)
    set1_p2 = set(player_2)
    if player_2_input == '':
        break
    if set1_p2 == set1 or set1_p2 == set2 or set1_p2 == set3 or set1_p2 == set4 or set1_p2 == set5 or set1_p2 == set6 or set1_p2 == set7:
        print("Player 2 won the game.")
        should_continue = input("Play again? 'y' or 'n': ")
        if should_continue == 'y':
            continue
    else:
        print(player_1)
        print(player_2)


