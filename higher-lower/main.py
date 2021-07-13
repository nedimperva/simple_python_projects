import random
from art import logo, vs
from gameData import data
import os

score = 0
should_end = False

#function for clearing command line screen
clear = lambda: os.system('cls') #instead of'cls' put 'clear' on Linux systems

#function to print game data
def print_data(a):
    a_name = a["name"]
    a_description = a["description"]
    a_country = a["country"]
    return(f"{a_name}, {a_description} from {a_country}")

#function to check answer
def check_answer(a_followers,b_followers, guess):
    a_followers = a["follower_count"]
    b_followers = b["follower_count"]
    if a_followers > b_followers:
        if guess == "a":
            return True
        else:
            return False

a = random.choice(data)
b = random.choice(data)
if a == b:
    b = random.choice(data)

while not should_end:
    print(logo)

    print(f"Compare A: {print_data(a)}")
    print(vs)
    print(f"Compare B: {print_data(b)}")

    guess = input("Who has more followers, A or B: ").lower()

    #check user answer
    is_correct = check_answer(a,b,guess)

    #give feedback 
    if is_correct:
        clear()
        score += 1
        print(f"You got it right, your current score is {score}")
        guess = a
        b = random.choice(data)
    else:
        print(f"The answer wasn't correct, final score is {score}")
        should_end = True

