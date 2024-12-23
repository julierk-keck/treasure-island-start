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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Your boat has docked at an island you believe to be the lost nation of Atlantis.  Can you find treasure or will death find you?")
step1 = input('You\'re standing on a sandy cove you see a climbable pile of rocks to the right and a sheer cliff to the left.  Do you use your climbing gear on the left or take the easier path to the right? Type "right" or "left" to continue. \n').lower()
if step1 == "left":
  step2 = input('You scale the cliff and after many difficult hours find a large, placid, beautiful lake at the top.  There is a small island in the middle of the lake.  Shall you swim the lake or wait to build a boat? (Type "swim" or "wait" to continue) \n').lower()
  if step2 == "wait":
    step3 = input('You build a raft from the forest trees and paddle across to the island.  In the middle of the island is some sort of temple.  From the middle are three doors.  One is red, one is yellow, and one is blue.  Which door do you choose? (Type "red", "yellow" or "blue" to continue) \n').lower()
    if step3 == "yellow":
      print('You have found the golden treasure.  Congratulations - You WIN!')
    elif step3 == "blue":
      print('An empty void comes from the door and you are sucked into it.  You are now trapped in the void forever.  Game Over.')
    elif step3 == "red":
      print(f'You open the door and are immediately engulfed in flames.  Game Over.')
    else:
      print('You have chosen a door that does not exist.  Game Over.')

  else:
    print(f"You attempt to swim across the lake but are attacked by a large trout.  Game over.")
else:
  print("As you climb the rocks, they suddenly begin shifting as a giant snake emerges from a cave and eats you whole.  Game over.")

