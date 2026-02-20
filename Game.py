        
import random

def game():
    print("You are playing a Game")
    score = random.randint(1, 100)
    
    # Fetch High score
    try:
        with open("Hiscore.txt", "r") as f:
            Hiscore = f.read()
    except FileNotFoundError:
        Hiscore = ""
    
    if Hiscore != "":
        Hiscore = int(Hiscore)
    else:
        Hiscore = 0
    
    print(f"Your Game Score is: {score}")
    
    if score > Hiscore:
        with open("Hiscore.txt", "w") as f:
            f.write(str(score))
    
    return score

game()         