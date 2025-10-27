import random

def game():
    print("You play a game...")
    score = random.randint(1,50)
    # Fetch the highScore.
    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore != ""):
            highscore = int(highscore)
        
        else:
            highscore = 0

    print(f"your score: {score}")
    if(score>highscore):
        with open("highscore.txt","w") as f:
            f.write(str(score))

    return score

game()
