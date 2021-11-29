from pynput import keyboard
from time import sleep
from random import randint

xlength = 48
ylength = 12

thenumber = 9
rightline = 4

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
  global rightline
  global thenumber
  #If nothing changes the "frame" is not re-printed
  #this reduces the screen glitches
  change = False
  jumping = False
  #Checks What Key is pressed
  if key == keyboard.Key.left:
    thenumber = thenumber - 1
    change = True
    if IsItAWall(thenumber, rightline):
      thenumber = thenumber + 1
      change = False
  elif key == keyboard.Key.right:
    thenumber = thenumber + 1
    change = True
    if IsItAWall(thenumber, rightline):
      thenumber = thenumber - 1
      change = False
  elif key == keyboard.Key.up:
    rightline = rightline - 1
    change = True
    if IsItAWall(thenumber, rightline):
      rightline = rightline + 1
      change = False
    jumping = True
  elif key == keyboard.Key.down:
    rightline = rightline + 1
    change = True
    if IsItAWall(thenumber, rightline):
      rightline = rightline - 1
      change = False
  if not IsItAWall(thenumber, (rightline + 1)) and not jumping:
    change = True
    rightline = rightline + 1
  #Prints
  if change:
    for line in range(1,ylength):
      for block in range(1,xlength):
        if block == thenumber and line == rightline:
          print("O", end = '')
        elif IsItAWall(block, line):
          print("█", end = '')
        else:
          print("~", end = '')
      print("")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
''''
for frame in range(0,100):
  for line in range(1,10):
    for block in range(0,40):
      if block == thenumber and line == rightline:
        print("█", end = '')
      else:
        print("0", end = '')
    print("")
  for i in range(0,2):
    print("") 
  sleep(0.1)
'''