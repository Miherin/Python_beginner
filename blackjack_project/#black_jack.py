############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##########################################

import random
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
house_hand = []

chosen_cards = random.sample(deck, 2)
sec_chosen_cards = random.sample(deck, 2)

user_hand.extend(chosen_cards)
house_hand.extend(sec_chosen_cards)

sum_userhand = sum(user_hand)
sum_househand = sum(house_hand)

print(f"Your cards {user_hand}: {sum_userhand} \nHouse cards [{house_hand[0]}] ")

while sum_userhand <= 21 or sum_househand <= 21:
        
    if sum_userhand == 21:
        if sum_househand == 21:
            print("Draw")
            break
        else:
            print("You win!")
            break
            
    elif sum_userhand > 21:
        print(f"You scored {sum_userhand} lost!")
        break
        
    elif sum_househand > 21:
        print(f"House {house_hand} scored {sum_househand} and lost!")
        break
        
    else:
        user_input = input("More cards? 'y' or 'n':  ")
        
        if user_input == 'y':
            third_random_card = random.sample(deck, 1)
            user_hand.extend(third_random_card)
            sum_userhand = sum(user_hand)
            
            for card in range(len(user_hand)):
                if sum_userhand > 21:
                    if user_hand[card] == 11:
                        user_hand[card] = 1
                        sum_userhand -= 10
            print(f"Your cards {user_hand}: {sum_userhand}")      
        
        elif user_input == 'n':
            add_card_house = random.sample(deck, 1)
            house_hand.extend(add_card_house)
            sum_househand = sum(house_hand)
            for card in range(len(house_hand)):
                if sum_househand > 21:
                    if house_hand[card] == 11:
                        house_hand[card] = 1
                        sum_househand -= 10
            
            if sum_househand == 21:
                print(f"Your cards {user_hand}: {sum_userhand} \nHouse cards [{house_hand}:{sum_househand}]\nHouse blackjack!")
                break
                
            while sum_househand < 16:
                add_card_house = random.sample(deck, 1)
                house_hand.extend(add_card_house)
                sum_househand = sum(house_hand)
                if sum_househand == sum_userhand:
                    print(f"Your cards {user_hand}: {sum_userhand} \nHouse cards [{house_hand}:{sum_househand}]\nDraw!")
                    break
                elif sum_househand > 21:
                    print(f"House {house_hand} scored {sum_househand} and lost!")
                    break
            
            if sum_househand >= 17 and  sum_househand <= 21:
                if sum_househand > sum_userhand:
                    print(f"Your cards {user_hand}: {sum_userhand} \nHouse cards [{house_hand}:{sum_househand}]\nHouse wins!")
                    break

        else:
            print("Please, type 'y' or 'n'")