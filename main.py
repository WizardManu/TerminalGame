from pynput import keyboard
from time import sleep
from random import randint
import os

os.system('cls' if os.name == 'nt' else 'clear')
xlength = 60
ylength = 12

Xcoord = 10
Ycoord = 4

WallTuples = [(1,11),(2,11),(3,10),(4,9),(5,8),
(6,8),(7,8),(9,8)]
SpikeTuples = [(8,9)]
PointTuples = [[8,7,True],[12,11,True]]
score = 0

def IsItAWall(xSpot, ySpot):
  for wall in range(len(WallTuples)):
    if WallTuples[wall][0] == xSpot:
      if ySpot == WallTuples[wall][1]:
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
def IAmSpiked(xSpot, ySpot):
  for spike in range(len(SpikeTuples)):
    if SpikeTuples[spike][0] == xSpot:
      if ySpot == SpikeTuples[spike][1]:
        return True
def DidIScore(xSpot, ySpot, Change):
  global PointTuples
  for point in range(len(PointTuples)):
    if PointTuples[point][0] == xSpot:
      if ySpot == PointTuples[point][1]:
          if PointTuples[point][2] == True:
            if Change:
              PointTuples[point][2] = False
              return True
            else:
              return True


def on_press(key):
  global Ycoord
  global Xcoord
  global score
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
    if not IsItAWall(Xcoord, Ycoord - 1) and IsItAWall(Xcoord, Ycoord + 1):
      Ycoord = Ycoord - 1
      change = True 
      jumping = True
      if not IsItAWall(Xcoord, Ycoord - 2):
        Ycoord = Ycoord - 1
  elif key == keyboard.Key.down:
    if not IsItAWall(Xcoord, Ycoord + 1):
      Ycoord = Ycoord + 1
      change = True
  else:
    return
  if not IsItAWall(Xcoord, (Ycoord + 1)) and not jumping:
    change = True
    Ycoord = Ycoord + 1
  if IAmSpiked(Xcoord, Ycoord):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Game Over")
    exit()
  if DidIScore(Xcoord, Ycoord, True):
    score = score + 1
  #Prints
  if change:
    room_str = ""
    for line in range(1,ylength):
      line_str = ""
      for block in range(1,xlength):
        if block == Xcoord and line == Ycoord:
          line_str += str(score)
        elif IsItAWall(block, line):
          line_str += "█"
        elif IAmSpiked(block, line):
          line_str += "X"
        elif DidIScore(block, line, False):
          line_str += 'P'
        else:
          line_str += "~"
      room_str += line_str
      room_str += "\n"
    os.system('cls' if os.name == 'nt' else 'clear')
    print(room_str)

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