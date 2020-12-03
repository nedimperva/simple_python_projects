from art import logo
import random

def one_dice():
    print("Rolling the dice...")
    print("The value is....")
    print(random.randint(1,6))

def two_dices():
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(1,6))
    print(random.randint(1,6))



print(logo)
print("Welcome to rolling dice simulator!")
roll_again = True
num = int(input("How many dices you want to roll? 1 or 2: "))
while roll_again:
    if num == 1:
        one_dice()
    else:
        two_dices()
    answer = input("Do you want to roll again? (y/n): ").lower()
    if answer == "y":
        roll_again = True
    else:
        roll_again = False
