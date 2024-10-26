
import random
print("Hey there! let me give you the instruction of the game")
print("It will be a Player vs CPU game")
print("Enter the number to choose the option \n 1.Rock \n 2.Paper \n 3.Scissor")
print("The winning instruction are:\n a) Rock vs Paper = paper wins \n b) Paper vs Scissor = Scissor wins \n c) Scissor vs Rock = Rock wins")
while True:
  choice = int(input("Enter the desired choice:")
  if choice == 1:
    choice_name = 'Rock'
  elif choice == 2:
    choice_name = 'Scissor'
  elif choice == 3:
    choice_name = 'Paper'
  else:
    print("Invalid Input! Goodbye")
    break
    
  comp_choice = random.randint(1,3)
  if comp_choice == 1:
    c_choice_name = 'Rock'
  if comp_choice == 2:
    c_choice_name = 'Scissor'
  if comp_choice == 3:
    c_choice_name = 'Paper'

  if choice == comp_choice:
    result = "DRAW"
  elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
    result = 'Paper'
  elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3):
    result = 'Rock'
  elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
    result = 'Scissors'

  if result == 'DRAW':
    print("It's a draw")
  elif result == choice_name:
    print("YEAH! YOU WINS!!!")
  else:
    print("OOPS! COMPUTER WINS!!!")
  print("Do you want to play again(y/n)?")
  ans = input.lower()
  if ans == 'n':
    break
