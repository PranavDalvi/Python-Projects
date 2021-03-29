# Snake Water Gun
import random

user = 0
computer = 0
turns = 10
lst = ["S", "W", "G"]
inp = ""
comp_inp = random.choice(lst)

while True:
    if turns == 0:
        if computer < user:
            print(f"Out of turns\nYour Score: {user}\nComputer Score: {computer}\n You Won!!!")
            break
        elif computer > user:
            print(f"Out of turns\nYour Score: {user}\nComputer Score: {computer}\n You Lose!!!")
            break
        elif computer == user:
            print(f"Out of turns\nYour Score: {user}\nComputer Score: {computer}\n Tie!!!")
            break

    inp = str(input("Please Enter S for Snake W for Water G for Gun: ")).upper()

    if inp == "S" and comp_inp == "W" or inp == "W" and comp_inp == "G" or inp == "G" and comp_inp == "S":
        user += 1
        turns -= 1
        print(f"Your Input: {inp} and Computer Input: {comp_inp}\nYou Won\n")
        comp_inp = random.choice(lst)

    elif inp == comp_inp:
        print(f"Your Input: {inp} and Computer Input: {comp_inp}\nTie!\n")
        turns -= 1
        comp_inp = random.choice(lst)

    elif inp == "W" and comp_inp == "S" or inp == "G" and comp_inp == "W" or inp == "S" and comp_inp == "G":
        computer += 1
        turns -= 1
        print(f"Your Input: {inp} and Computer Input: {comp_inp}\nYou Lose\n")
        comp_inp = random.choice(lst)
