# SNAKE WATER GUN CHAMPION
'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice:")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("Its Draw📍")

else:
    if(computer == -1 and you == 1):
        print("You win!🏆")  # fetching the given information go to the even place and create a short logic.

    elif(computer == -1 and you == 0):
        print("You lose!😥")

    elif(computer == 1 and you == -1):
        print("You lose!😥")

    elif(computer == 1 and you == 0):
        print("You win!🏆")

    elif(computer == 0 and you == -1):
        print("You win!🏆")

    elif(computer == 0 and you == 1):
        print("You lose😥")

    else:
        print("Something went wrong❌")