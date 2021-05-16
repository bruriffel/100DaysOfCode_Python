import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,2)

choices = [rock, paper, scissors]

if player >= 3 or player < 0:
  print("Invalid option. Please try again")
else:
 
  print(choices[player])
  
  print("Computer chose:")

  print(choices[computer])
 
  if player == computer:
    print("It's a draw.")
  elif player == 0 and computer == 1:
    print("You lose.")
  elif player == 1 and computer == 2:
    print("You lose.")
  elif player == 2 and computer == 0:
    print("You lose.")
  else:
    print("You win.")
