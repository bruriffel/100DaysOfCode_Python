print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

crossroad = input(str("You're at a crossroad and need to choose between left or right. Where do you want to go?\n")).lower()

if crossroad == "left":
  lake = input(str("Nice walk! You come to a lake with an island in the middle. There is a boat coming in 1 hour. Type 'wait' to wait for the boat or 'swim' to swim across.\n")).lower()
  if lake == "wait":
    door = input(str("You've arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Only one door will take you to the treasure. Which color do you choose?\n")).lower()
    if door == "red":
      print("Burned by fire. Game Over.")
    elif door == "blue":
      print("Eaten by beasts. Game over.")
    elif door == "yellow":
      print("You found the treasure! You Win!")
    else:
      print("This door doesn't exist. Game Over.")
  else:
    print("Attacked by a crocodile. Game over.")
else:
  print("Fall into a hole. Game Over.")
