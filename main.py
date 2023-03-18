import random, os, time


def dice_roll(side):
  result = random.randint(1, side)
  return result

def health():
  health_stats = ((dice_roll(6)*dice_roll(12))/2)+10
  return health_stats

def strength():
  strength_stats = ((dice_roll(6)*dice_roll(12))/2)+12
  return strength_stats

  
print("-- ⚔️ BATTLE SIMULATOR ⚔️ --")
char1_name = input("Enter the first name:  ")
char1_type = input("Choose a type of character (human, imp, wizard, elf, etc.):  ")
char1_health = health()
char1_strength = strength()
print()
print(char1_name, " the ", char1_type)
print()
print("HEALTH: ", char1_health)
print("STRENGTH: ", char1_strength)
print()
print("Let's meet the Challenger")
print()

char2_name = input("Enter the first name:  ")
char2_type = input("Choose a type of character (human, imp, wizard, elf, etc.):  ")
char2_health = health()
char2_strength = strength()
print()
print(char2_name, " the ", char2_type)
print()
print("HEALTH: ", char2_health)
print("STRENGTH: ", char2_strength)
print()

round = 1
winner = None
winner_type = None

while True:
  time.sleep(7)
  os.system("clear")
  print("-- ⚔️ BATTLE SIMULATOR ⚔️ --")
  print()
  print("FIGHT!!!!!!")
  
  char1_dice = dice_roll(6)
  char2_dice = dice_roll(6)

  diff = abs(char1_strength - char2_strength) + 1

  if char1_dice > char2_dice:
    char2_health -= diff
    if round == 1:
      print(char1_name, "throws the first blow")
    else:
      print(char1_name, "wins this round", round)
  elif char2_dice > char1_dice:
    char1_health -= diff
    if round == 1:
      print(char2_name, "throws the first blow")
    else:
      print(char2_name, "wins this round", round)
  else:
    print("The Challengers are unable to land a hit. It's a draawww!!!!", round)
    
    print()
    print(char1_name)
    print("HEALTH: ", char1_health)
    print()

    print()
    print(char2_name)
    print("HEALTH: ", char2_health)
    print()

    if char1_health <= 0:
      print(char1_name, "died valiantly in battle!")
      winner = char2_name
      winner_type = char2_type
      break
    elif char2_health <= 0:
      print(char2_name, "died valiantly in battle!")
      winner = char1_name
      winner_type = char1_type
      break
    else:
      print("And the Battle goes on!!!!!")
      round += 1


time.sleep(7)
os.system("clear")
print("-- ⚔️ BATTLE SIMULATOR ⚔️ --")
print()
print("Our Winner is.............. ", winner, "the", winner_type)
print("Congratulations ", winner, "has won in", round, "round(s)")