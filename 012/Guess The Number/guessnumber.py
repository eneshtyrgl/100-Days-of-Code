import random
import os
from time import sleep
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")
    return play_again()

def set_difficulty():
  sleep(0.5)
  difficulty = input("Choose a difficulty. Type [E]asy or [H]ard: ").lower()
  if difficulty == "e":
    return EASY_LEVEL_TURNS
  elif difficulty == "h":
    return HARD_LEVEL_TURNS
  else: 
    sleep(0.5)
    print("Wrong choice. Please try again.")
    set_difficulty()

def play_again():
    sleep(0.5)
    again = input("Do you want to play again? Type [Y]es or [N]o: ").lower()
    if again == "y":
        sleep(0.5)
        os.system('cls')
        game()
    else:
        sleep(0.5)
        print("Bye!")
        sleep(3)
        exit()

def game():
  sleep(0.5)
  print(logo)
  sleep(0.5)
  print("Welcome to the Number Guessing Game!")
  sleep(0.5)
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100) 
  turns = set_difficulty()
  guess = 0
  while guess != answer:
    sleep(0.5)
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check(guess, answer, turns)
    if turns == 0:
      sleep(0.5)
      print("You've run out of guesses, you lose.")
      sleep(0.5)
      print(f"The number was: {answer}")
      return play_again()
    elif guess != answer:
      sleep(0.5)
      print("Guess again.")

game()
