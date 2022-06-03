import random

# Welcome intro

print("Welcome to Rock, Paper, Scissors!")
print(".................................")
player_name = input("What is your name? ")
print("Hello " + player_name + " let's play Rock, Paper, Scissors")
print("Instructions for Rock, Paper, Scissors : ")
print()
print("Rock crushes Scissors")
print("Scissors cuts Paper")
print("Paper covers Rock")
print()



# Game Menu
print()
print("Let's Play!!!")

def Choose_Option():
    player_choice = input("Choose Rock, Paper or Scissors: ")
    if player_choice in ["Rock", "rock", "r", "R"]:
        player_choice = "r"
    elif player_choice in ["Paper", "paper", "p", "P"]:
        player_choice = "p"
    elif player_choice in ["Scissors", "scissors", "s", "S"]:
        player_choice = "s"
    else:
        print("I dont understand, try again")
        Choose_Option()
    return player_choice

def Computer_Option():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice = "r"
    elif computer_choice == 2:
        computer_choice = "p"
    elif computer_choice == 3:
        computer_choice = "s"
    return computer_choice

while True:
    print("")
    player_choice = Choose_Option()
    computer_choice = Computer_Option()
    print("")

    if player_choice == computer_choice:
        print("It's a tie!")
        tie_score += 1

    elif player_choice == "r":
         if computer_choice == "p":
          print("Computer chose paper and won this round, you lost!")
          computer_score += 1
          print("computer_score: " + str(computer_score) + "\n" + "Your score: " + str(player_score))

         if computer_choice == "s":
          print("Computer chose scissors. You won this round!")
          player_score += 1
          print("computer_score: " + str(computer_score) + "\n" + "Your score: " + str(player_score))


    elif player_choice == "p":
         if computer_choice == "r":
          print("Computer chose rock. You won this round!")
          player_score += 1
          print("computer_score: " + str(computer_score) + "\n" + "Your_score: " + str(player_score))

         if computer_choice == "s":
          print("Computer chose scissors. You won this round!")
          player_score += 1
          print("computer_score: " + str(computer_score) + "\n" + "Your_score: " + str(player_score))


    else:
         if computer_pick == "p":
          print("Computer chose paper. You won this round!")
          player_score += 1
          print("computer_score: " + str(computer_score) + "\n" + "Your_score: " + str(player_score))

         if computer_choice == "s":
          print("Computer chose rock. You won this round!")
          player_score += 1
          print("computer_score: " + str(computer_score) + "\n" + "Your_score: " + str(player_score))

    if player_score == 3:
        print ("You won! Best three out of 5!")
        break

    if computer_score == 3:
        print ("Computer won! Best three out of 5! You lost this game")
        break







 

