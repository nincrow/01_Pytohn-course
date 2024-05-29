import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("YOU LOSE!")
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("YOU WON!!")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("YOU LOSE!")
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("YOU WON!!")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("YOU LOSE!")
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("YOU WON!!")
    
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("THANKS FOR PLAYING!!")
print("BYE!!")