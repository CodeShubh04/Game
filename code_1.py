from random import randint
t = ["Rock", "Paper", "Scissor"]
computer = t[randint(0,2)]
player = False
while player == False:
    player = input("Rock, Paper, Scissor?")
    print("computer choase",computer)
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissor":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissor":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    player = False
    computer = t[randint(0,2)]
