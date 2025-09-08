# Heads or Tails
import random
#

# # Bankers Roulette
# players = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# # todaysWinner = random.choice(players)
# todaysWinner = random.randint(0, len(players) - 1)
# # print(f"{todaysWinner} will pay the bill today.")
# print(f"{players[todaysWinner]} will pay the bill today.")

# Rock, Paper, Scissors
gameMoves = ["rock", "paper", "scissors"]
userMove = int(input("Enter the corresponding number for your move: 0 for Rock, 1 for Paper, 2 for Scissors. "))
computerMove = random.randint(0, 2)
print(f"Your move: {gameMoves[userMove]}")
print(f"Computer's move: {gameMoves[computerMove]}")
if userMove == computerMove:
    print("It's a draw!")
elif (userMove == 0 and computerMove == 2) or (userMove == 1 and computerMove == 0) or (userMove == 2 and computerMove == 1):
    print("You win!")
else:
    print("You lose!")

