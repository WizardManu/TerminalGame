from pynput import keyboard
from time import sleep
from random import randint

thenumber = 9
rightline = 4

xwalls = [4,4,3,6,7,8,5,6,10]
ywalls = [1,6,2,2,3,4,5,6,9]


def IsItAWall(xSpot, ySpot):
  for wallX in range(len(xwalls)):
    if xwalls[wallX] == xSpot:
      if ySpot == ywalls[wallX]:
        return True
  if ySpot >= 10:
    return True
  return(False)

def on_press(key):
  global rightline
  global thenumber
  if key == keyboard.Key.left:
    thenumber = thenumber - 1
    if IsItAWall(thenumber, rightline):
      thenumber = thenumber + 1
  elif key == keyboard.Key.right:
    thenumber = thenumber + 1
    if IsItAWall(thenumber, rightline):
      thenumber = thenumber - 1
  elif key == keyboard.Key.up:
    rightline = rightline - 1
    if IsItAWall(thenumber, rightline):
      rightline = rightline + 1
  elif key == keyboard.Key.down:
    rightline = rightline + 1
    if IsItAWall(thenumber, rightline):
      rightline = rightline - 1
  if not IsItAWall(thenumber, (rightline - 1)):
    rightline = rightline + 1
  for line in range(1,10):
    for block in range(0,40):
      if block == thenumber and line == rightline:
        print("O", end = '')
      elif IsItAWall(block, line):
        print("█", end = '')
      else:
        print("~", end = '')
    print("")
  for i in range(0,2):
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