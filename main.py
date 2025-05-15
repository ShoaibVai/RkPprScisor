import random
import os

def play_game():
    plyrScore = 0
    comScore = 0
    n = 0

    round = int(input("How many rounds do you want to play?\n"))
    os.system("cls")

    def comThink():
        com = random.randint(1, 3)
        return com

    def printComChoice():
        if (com == 1):
            print("Computer Chose ROCK!!!\n")
        if (com == 2):
            print("Computer Chose SCISSOR!!!\n")
        if (com == 3):
            print("Computer Chose PAPER!!!\n")

    def printPlyrChoice():
        if (plyr == 1):
            print("Player Chose ROCK!!!\n")
        if (plyr == 2):
            print("Player Chose SCISSOR!!!\n")
        if (plyr == 3):
            print("Player Chose PAPER!!!\n")

    # 0=rock
    # 1=scissor
    # 2=paper
    while (n < round):

        print(f"Round {n + 1}")
        print(f"Computer Score: {comScore}")
        print(f"Player Score: {plyrScore}")
        com = comThink()
        plyr = int(input('''Choose Your Move:\n1=rock\n2=scissor\n3=paper\n'''))
        if (plyr >= 1 and plyr <= 3):
            n = n + 1
            if (com == plyr):
                os.system("cls")  # clears termianl
                printComChoice()
                printPlyrChoice()
                print(f"Round {n} Tie\n")
            elif (com == 1 and plyr == 3) or \
                    (com == 2 and plyr == 1) or \
                    (com == 3 and plyr == 2):
                os.system("cls")  # clears termianl
                printComChoice()
                printPlyrChoice()
                print(f"Round {n} WON!!\n")
                plyrScore = plyrScore + 1
            else:
                os.system("cls")  # clears termianl
                printComChoice()
                printPlyrChoice()
                print(f"Round {n} LOSE!!\n")
                comScore = comScore + 1
        else:
            print("Invald User Input.Please choose from user 1 to 3")
    # Final result
    if (comScore == plyrScore):
        print(f"Computer Score: {comScore}")
        print(f"Player Score: {plyrScore}")
        print("MATCH is TIEEEEE!! That was a furious battle")
    elif (comScore < plyrScore):
        print(f"Computer Score: {comScore}")
        print(f"Player Score: {plyrScore}")
        print("MATCH WOOOOOON by Player!!!!!!")
    else:
        print(f"Computer Score: {comScore}")
        print(f"Player Score: {plyrScore}")
        print("BOOOOOOO!! YOU LOOOST!!! :v ")

    restart = input("Press \"Enter\" to Finish the Match or Press 'R' to restart the programme\n")
    if restart.lower() == 'r':
        play_game()

play_game()