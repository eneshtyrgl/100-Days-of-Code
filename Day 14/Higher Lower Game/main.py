import random
import os
from time import sleep
from art import logo
from art import vs
from game_data import data
#----------------------------------------------------------------------------------------------------------#
def pick():
    pick = data.pop(0)
    return pick
#----------------------------------------------------------------------------------------------------------#
def compare(a, b):
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    fallower_a = a['follower_count']
    fallower_b = b['follower_count']
    while answer != "a" and answer != "b":
        print("Invalid answer. Please try again.")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if fallower_a > fallower_b:
        return answer == "a"
    else:
        return answer == "b"
#----------------------------------------------------------------------------------------------------------#
def play_again():
    again = input("Do you want to play again? Type [Y]es or [N]o: ").lower()
    if again == "y":
        os.system('cls')
        game()
    else:
        print("Bye!")
        exit()
#----------------------------------------------------------------------------------------------------------#
def game():
    print(logo)
    score = 0
    game_continue = True
    random.shuffle(data)
    a = pick()
    b = pick()
    while game_continue:
        a = b
        b = pick()
        # print(f"A: {a['follower_count']}")
        # print(f"B: {b['follower_count']}")
        print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")
        result = compare(a, b)
        os.system('cls')
        print(logo)
        if result:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
            play_again()

#----------------------------------------------------------------------------------------------------------#
game()