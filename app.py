#create a complete rock, paper scissors game, the user choses one of the three options and other user choses one of the three options, then the winner is displayed
#rock win to scissors, scissors win to paper, paper win to rock, if both choses the same option, it's a tie
#player must chose one of the three options, if not, the game will ask again until the user choses one of the three options
#player can chose to play again or not, if not, the game will end
#player need to confirm if he wants to play the chosen option, if not, the game will ask again until the user confirms
#player can view the score
#player must be informed if he won, lost or tied
#the game must control the entry data, if the user enters a wrong data or caps, the game will ask again until the user enters a correct data

from random import randint

player_wins = 0
computer_wins = 0

print("...rock...")
print("...paper...")
print("...scissors...")

while True:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("Player, make your move:")
    player = input()
    player = player.lower()
    if player == "quit" or player == "q":
        break
    random_number = randint(0,2)
    if random_number == 0:
        computer = "rock"
    elif random_number == 1:
        computer = "paper"
    else: 
        computer = "scissors"
    print(f"Computer plays {computer}")
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
            computer_wins += 1
    else:
        print("Please enter a valid move!")