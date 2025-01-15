import os 
import random
from time import sleep
from art import logo

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

def hand(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        control(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

def hit(hand):
    control(deck)
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

def score(hand):
    score = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            score += 10
        elif card == "A":
            if score >= 11:
                score+= 1
            else:
                score+= 11
        else:
            score += card
    return score

def blackjack(player_hand, computer_hand):
    if score(player_hand) == 21:
        print ("You got a Blackjack!\n")
        play_again()
    elif score(computer_hand) == 21:
        print ("You lose. The computer got a Blackjack.\n")
        play_again()

def result(player_hand, computer_hand):
    if score(player_hand) == 21:
        print(f"Your cards: {str(player_hand)}, final score: {str(score(player_hand))}")
        print(f"Computer's: {str(computer_hand)}, final score: {str(score(computer_hand))}")
        print ("You got a Blackjack!\n")
    elif score(computer_hand) == 21:
        print(f"Your cards: {str(player_hand)}, final score: {str(score(player_hand))}")
        print(f"Computer's: {str(computer_hand)}, final score: {str(score(computer_hand))}")
        print ("You lose. The computer got a Blackjack.\n")
    elif score(player_hand) > 21:
        print(f"Your cards: {str(player_hand)}, final score: {str(score(player_hand))}")
        print(f"Computer's: {str(computer_hand)}, final score: {str(score(computer_hand))}")
        print ("You busted. You lose.\n")
    elif score(computer_hand) > 21:
        print(f"Your cards: {str(player_hand)}, final score: {str(score(player_hand))}")
        print(f"Computer's: {str(computer_hand)}, final score: {str(score(computer_hand))}")       
        print ("Computer busts. You win!\n")
    elif score(player_hand) < score(computer_hand):
        print(f"Your cards: {str(player_hand)}, final score: {str(score(player_hand))}")
        print(f"Computer's: {str(computer_hand)}, final score: {str(score(computer_hand))}")
        print ("Your score isn't higher than the cpmputer. You lose.\n")
    elif score(player_hand) > score(computer_hand):
        print(f"Your cards: {str(player_hand)}, final score: {str(score(player_hand))}")
        print(f"Computer's: {str(computer_hand)}, final score: {str(score(computer_hand))}")
        print ("Your score is higher than the computer. You win\n")

def play_again():
    again = input("Do you want to play a game of Blackjack? Type 'Y' or 'N': ").lower()
    if again == "y":
        os.system('cls')
        game()
    else:
        print("Bye!")
        sleep(3)
        exit()

def control(list):
    if list == []:
        print("Cards finished")
        more_game = input("Would you like to continue? Type 'Y' or 'N': ").lower()
        if more_game == "y":
            global deck
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
            os.system('cls')
            game()
        else:
            print("Bye!")
            sleep(3)
            exit()

def game():  
    player_hand = hand(deck)
    computer_hand = hand(deck)
    print(logo)
    print(f"Your cards: {str(player_hand)}, current score: {str(score(player_hand))}")
    print(f"Computer's first card: {str(computer_hand[0])}")
    blackjack(player_hand, computer_hand)
    choice = 0
    quit = False
    while not quit:
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        if choice == "h":
            hit(player_hand)
            print(player_hand)
            print(f"Hand total: {str(score(player_hand))}")
            if score(player_hand) > 21:
                print('You busted')
                play_again()
        elif choice == "s":
            for i in range(5):
                while score(computer_hand) < 17:
                    hit(computer_hand)
                    sleep(0.5)
                    print(computer_hand)
                    if score(computer_hand) > 21:
                        print('Dealer busts, you win!')
                        play_again()
            result(player_hand, computer_hand)    
            play_again() 
        elif choice == "q":
            print("Bye!")
            sleep(3)
            quit=True
            exit()

game()