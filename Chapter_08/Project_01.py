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
   if((computer - you )== -1 or (computer - you )== 2):
       print("You lose😥")
   else:
       print("You Win🏆")