import random

# Map:
#          |------|------|
#          |      |      |
# Start ---|------|------|
#          |      |      |
#          |------|------|

# Map with names:
#        c1c1-----|------|
#          |      |      |
# Start ---|------|------|
#          |      |      |
#        c1c2-----|------|

#-----------------------------------------------------------------------------------------------------------------------------------------
def c1c1():
  print("You run down the path and it leads into a larger cave.")
  input()
  print("There is an agressive goblin in the cave!")
  input()
  c1c1ch = input("Do you try to run away or stay and fight? (run away/fight)")
  
  m = 1
  while (m == 1):
    if c1c1ch/lower() == "run away":
      runAway()
      

#-----------------------------------------------------------------------------------------------------------------------------------------
print('Welcome to the python version of the game MountainsAndMonsters.')
print("From now on, after most lines of text you will have to press a key to continue.")
input()

print("Your journey starts at the beginings of a cave, one of the only entrances into Mount Procerus.")
input()
print("However, you soon discover that further into the cave it splits into two paths.")

n = 1
while(n == 1)
  c1 = input("Do you take the left or the right path? (left/right): ")
  
  if c1.lower() == "left":
    c1c1()
    n = 2
  elif c1.lower() == "right":
    c1c2()
    n = 2
  else:
    print("That is not a choice!")
