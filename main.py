import random
wincus = 0
rpss = ["rock", "paper", "scissors"]
while wincus != 3 or -3:
  print("<=,------------,=>")
  print()
  print("  |    rock    |")
  print()
  print("  |    paper   |")
  print()
  print("  |  scissors  |")
  print()
  print("  |   shoot!   |")
  print()
  print("<='------------'=>")
  print()
  userchoice = input()
  cpchoice = random.choice(rpss)
  print()
  print(cpchoice)
  print()
  if str(userchoice) == str(cpchoice):
    print("  |user choice: %s|" % userchoice)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("you appear to have met your match. no matter how much or how hard you fight, it ends in a tie.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("  |computer choice: %s|" % cpchoice)
    print()
    print(" score count: [%s]" % wincus)
  elif str(userchoice) == "rock" and str(cpchoice) == "paper":
    print("  |user choice: %s|" % userchoice)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("The paper lunges at the stone, it covers the stones entire   surface area. the computer wins")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("  |computer choice: %s|" % cpchoice)
    print()
    wincus -= 1
    print(" score count: [%s]" % wincus)
  elif str(userchoice) == "rock" and str(cpchoice) == "scissors":
    print("  |user choice: %s|" % userchoice)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You jump and crush the opponent in one fluid movement. You   win")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("  |computer choice: %s|" % cpchoice)
    print()
    wincus += 1
    print(" score count: [%s]" % wincus)
  elif str(userchoice) == "scissors" and str(cpchoice) == "rock":
    print("  |user choice: %s|" % userchoice)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("The rock jumps and crushes you in one fluid movement. The   computer wins")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("  |computer choice: %s|" % cpchoice)
    print()
    wincus -= 1
    print(" score count: [%s]" % wincus)
  elif str(userchoice) == "scissors" and str(cpchoice) == "paper":
    print("  |user choice: %s|" % userchoice)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You slice through the sheet of paper with ease. you win")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("  |computer choice: %s|" % cpchoice)
    print()
    wincus += 1
    print(" score count: [%s]" % wincus)
  elif str(userchoice) == "paper" and str(cpchoice) == "rock":
    print("  |user choice: %s|" % userchoice)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You lunge at the stone, you cover the rock's entire surface area. You win")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("  |computer choice: %s|" % cpchoice)
    print()
    wincus += 1
    print(" score count: [%s]" % wincus)
  elif str(userchoice) == "paper" and str(cpchoice) == "scissors":
    print("  |user choice: %s|" % userchoice)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("The scissors slices through you with ease. the computer wins")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("  |computer choice: %s|" % cpchoice)
    print()
    wincus -= 1
    print(" score count: [%s]" % wincus)
  elif str(userchoice) != "rock" or "paper" or "scissors":
    print("  |Error 404|")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("An error has occured")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("  |Error 404|")
    print()
    wincus += 0
    print(" score count: [%s]" % wincus)
  if wincus == 3:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("A winner is you")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    break
  elif wincus == -3:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Congratulations! You've lost to a glorified toaster")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    break
