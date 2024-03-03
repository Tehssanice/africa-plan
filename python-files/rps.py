import random


# ROCK, PAPER, SCISSORS

# 0 Wins, 0 Losses, 0 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# p
# PAPER versus...
# PAPER
# It is a tie!
# 0 Wins, 1 Losses, 1 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# s
# SCISSORS versus...
# PAPER
# You win!
# 1 Wins, 1 Losses, 1 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit


# options = ["r", "p", "s"]

# while True:
#     computer_choice = random.choice(options)
#     user_choice = input(
#         "Enter your choice ((r)ock, (p)aper, (s)cissors or (q)uit): ").lower()
#     if user_choice in options:
#       if user_choice == computer_choice:
#         print(f"User choice is {user_choice}")
#         print(f" Computer choice is :{computer_choice}")
#         print("It's a Tie")
#       elif user_choice == 'r' and computer_choice == 'p':
#         print(f"User choice is {user_choice}")
#         print(f" Computer choice is :{computer_choice}")
#         print("Computer wins")
#       elif user_choice == 'p' and computer_choice == 's':
#         print(f"User choice is {user_choice}")
#         print(f" Computer choice is :{computer_choice}")
#         print("Computer wins")
#       elif user_choice == 's' and computer_choice == 'r':
#         print(f"User choice is {user_choice}")
#         print(f" Computer choice is :{computer_choice}")
#         print("Computer wins")
#       elif user_choice == 's' and computer_choice == 'p':
#         print(f"User choice is {user_choice}")
#         print(f" Computer choice is :{computer_choice}")
#         print("User wins")
#       elif user_choice == 'r' and computer_choice == 's':
#         print(f"User choice is {user_choice}")
#         print(f" Computer choice is :{computer_choice}")
#         print("User wins")
#       elif user_choice == 'p' and computer_choice == 'r':
#         print(f"User choice is {user_choice}")
#         print(f" Computer choice is :{computer_choice}")
#         print("User wins")
#     elif user_choice == 'q':
#       break
#     else:
#         print("Invalid choice")


########################################### OR THIS METHOD CAN WORK ###################################


wins = 0
losses = 0
ties = 0

while True:
    user_choice = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    if user_choice not in ['r', 'p', 's', 'q']:
        print('Invalid choice!')
        continue
    if user_choice == 'q':
        print(
            f"Thanks for playing. Final score: Wins - {wins}, Losses - {losses}, Ties - {ties}")
        break

    computer_choice = random.choice(["r", "p", "s"])

    print("Your choice:", user_choice)
    print("Computer's choice:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
        ties += 1

    elif (user_choice == "r" and computer_choice == "s") or \
        (user_choice == "s" and computer_choice == "p") or \
            (user_choice == "p" and computer_choice == "r"):
        print("You win!")
        wins += 1

    else:
        print("You loose! CRY CRY BABY NTOORRR!!!")
        losses += 1
