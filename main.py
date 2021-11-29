from pynput import keyboard
from time import sleep
from random import randint

xlength = 60
ylength = 20

Xcoord = 9
Ycoord = 4

xwalls = [4,4,3,6,7,8,5,6,10]
ywalls = [1,6,2,2,3,4,5,6,9]


def IsItAWall(xSpot, ySpot):
  for wallX in range(len(xwalls)):
    if xwalls[wallX] == xSpot:
      if ySpot == ywalls[wallX]:
        return True
  if ySpot >= ylength:
    return True
  elif ySpot <= 0:
    return True
  elif xSpot <= 0:
    return True
  elif xSpot >= xlength:
    return True
  return(False)

def on_press(key):
  global Ycoord
  global Xcoord
  #If nothing changes the "frame" is not re-printed
  #this reduces the screen glitches
  change = False
  jumping = False
  #Checks What Key is pressed
  if key == keyboard.Key.left:
    if not IsItAWall(Xcoord - 1, Ycoord):
      Xcoord = Xcoord - 1
      change = True
  elif key == keyboard.Key.right:
    if not IsItAWall(Xcoord + 1, Ycoord):
      Xcoord = Xcoord + 1
      change = True
  elif key == keyboard.Key.up:
    if not IsItAWall(Xcoord, Ycoord - 1):
      Ycoord = Ycoord - 1
      change = True 
    jumping = True
  elif key == keyboard.Key.down:
    if not IsItAWall(Xcoord, Ycoord + 1):
      Ycoord = Ycoord + 1
      change = True
  else:
    return
  if not IsItAWall(Xcoord, (Ycoord + 1)) and not jumping:
    change = True
    Ycoord = Ycoord + 1
  #Prints
  if change:
    for line in range(1,ylength):
      for block in range(1,xlength):
        line_str = ""
        if block == Xcoord and line == Ycoord:
          line_str += "O"
        elif IsItAWall(block, line):
          line_str += "█"
        else:
          line_str += "~"
      print(line_str)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
''''
for frame in range(0,100):
  for line in range(1,10):
    for block in range(0,40):
      if block == Xcoord and line == Ycoord:
        print("█", end = '')
      else:
        print("0", end = '')
    print("")
  for i in range(0,2):
    print("") 
  sleep(0.1)
'''