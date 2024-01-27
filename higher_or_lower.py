from art import logo, vs
from data import data
import random
import os


def start_game():
    print(logo)
    print(f"Your score is {score}.")
    thing_a()
    print(f"A: {name_a}, {description_a} from {country_a}.")
    print(vs)
    thing_b()
    print(f"B: {name_b}, {description_b} from {country_b}.")


def thing_a():
    global name_a, description_a, country_a, follower_count_a
    a = random.choice(data)
    name_a = a["name"]
    description_a = a["description"]
    country_a = a["country"]
    follower_count_a = a["follower_count"]


def thing_b():
    global name_b, description_b, country_b, follower_count_b
    b = random.choice(data)
    name_b = b["name"]
    description_b = b["description"]
    country_b = b["country"]
    follower_count_b = b["follower_count"]


game_continues = True

while game_continues:
    alive = True
    score = 0
    while alive:
        os.system('cls')
        start_game()
        guess = input("Who has more followers? Type 'A' or 'B': ")
        if guess == 'a' and (follower_count_a > follower_count_b):
            score += 1
            print("xd")
        elif guess == 'b' and (follower_count_a < follower_count_b):
            score += 1
            print("xd")
        else:
            alive = False
    os.system('cls')
    print(logo)
    print(f"You lost, your score was {score}.")
    if input("Do you want to continue? Enter 'y' if yes or 'n' if no. ") == 'n':
        game_continues = False
