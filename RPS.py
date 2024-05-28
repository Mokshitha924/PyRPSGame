import random
ComputerScore=0
PlayerScore=0
arr=["Rock","Paper","Scissors"]
inPlay=True
def gamePlay():
    global inPlay
    global ComputerScore
    global PlayerScore
    while inPlay:
        global ComputerScore
        global PlayerScore
        player=input("Rock Paper or Scissor?").capitalize()
        computer=random.choice(arr).capitalize()
        print(f"You Selected {player}vs Computer Selected {computer}")
        if player==computer:
            print("Tie Game")
        elif player=="Rock":
            if computer=="Paper":
                print("You lose")
                ComputerScore+=1
            else:
                print("You win")
                PlayerScore+=1
        elif player=="Paper":
            if computer=="Scissor":
                print("You lose")
                ComputerScore+=1
            else:
                print("You win")
                PlayerScore+=1
        elif player=="Scissor":
            if computer=="Rock":
                print("You lose")
                ComputerScore+=1
            else:
                print("You win")
                PlayerScore+=1
        print(f"Computer Score:{ComputerScore} vs Player Score:{PlayerScore}")
        inPlay=input("Roll Again? (yes/no)")
        if inPlay=="no":
            ##print("Game Over")
            ##print(f"Computer Score:{ComputerScore} vs Player Score:{PlayerScore}")
            break
gamePlay()
print("Game over")
print(f"Computer Score:{ComputerScore} vs Player Score:{PlayerScore}")
