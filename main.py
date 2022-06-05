from console import Console
from threading import Thread
from time import sleep
import sys

debugMode = True if '--debug' in sys.argv else False
console = Console(debugMode=debugMode)
basemap = str(console.mapRows)
curmap = console.mapRows
tps = 20

keymap = {
 'moveUp': ['w', 'Up'],
 'moveDown': ['s', 'Down'],
 'moveLeft': ['a', 'Left'],
 'moveRight': ['d', 'Right'],
 'actionInteract': ['1'],
 'actionCheck': ['2'],
 'actionMenu': ['3']
}

positions = {
 'characterOld': ['C', 3],
 'character': ['C', 3]
}

directions = {
 'characterOld': ['up'],
 'character': ['up']
}

blocked = [
 # Wall Blocks
 ['A', '*'], ['*', 1], ['E', '*'], ['*', 9]
]
# Change * shortcut to A-E and 1-10
blockedTemp = blocked
for block in blocked:
 if block[0] == '*':
  for i in range(5):blockedTemp.append([chr(i+65), block[1]])
 if block[1] == '*':
  for i in range(9):blockedTemp.append([block[0], i+1])
del blockedTemp

def letterDecrement(char:str): return changePrevention(chr(ord(char)-1))
def letterIncrement(char:str): return changePrevention(chr(ord(char)+1))
def numberDecrement(targ:int): return changePrevention(targ-2)
def numberIncrement(targ:int): return changePrevention(targ+2)
def changePrevention(targ):
 # Out of Bounds Check
 if not targ in ['A','B','C','D','E',1,2,3,4,5,6,7,8,9,10]: return 'preventMove'
 else:
  return targ

def queryDescType(line:str, number:int, autoclear:bool, avoidRows:list=[]):
 curword = ''
 for letter in line:
  curword += letter
  console.descRows[str(number)] = '> '+curword+'\n'
  for row in console.descRows:
   if str(row) != str(number) and int(row) > number: console.descRows[row] = '> '+' '*len(curword)+'\n'
  console.updateElements()
  sleep(1/ ( len(line) ) )
 if autoclear:
  sleep(1/tps*4)
  for row in console.descRows:
   console.descRows[row] = '> \n'

def checkPrevent(target:str, check): return target if check(target) == 'preventMove' else check(target)

def updatePositions():
 curmap = eval(basemap)
 # blocked Check on Character
 for block in blocked:
  if positions['character'] == block:
   positions['character'] = eval(str(positions['characterOld']))
 # Update Character
 charver = positions['character'][0].lower()
 charhor = positions['character'][1]+1
 char    = '▲'
 if directions['character'][0] == 'up': char = '▲'
 if directions['character'][0] == 'down': char = '▼'
 if directions['character'][0] == 'left': char = '◄'
 if directions['character'][0] == 'right': char = '►'
 curmap[charver] = curmap[charver][:charhor]+char+curmap[charver][charhor+1:]
 # Update Map
 console.mapRows = curmap
 console.updateElements()

def loop():
 while True:
  # Handlers
  positions['characterOld'] = eval(str(positions['character']))
  ## Movement
  ### Move Up
  if console.activeKey in keymap['moveUp']: 
   positions['character'][0]=checkPrevent(positions['character'][0],letterDecrement)
   directions['character'][0] = 'up'
  ### Move Down
  if console.activeKey in keymap['moveDown']: 
   positions['character'][0]=checkPrevent(positions['character'][0],letterIncrement)
   directions['character'][0] = 'down'
  ### Move Left
  if console.activeKey in keymap['moveLeft']: 
   positions['character'][1]=checkPrevent(positions['character'][1],numberDecrement)
   directions['character'][0] = 'left'
  ### Move Right
  if console.activeKey in keymap['moveRight']: 
   positions['character'][1]=checkPrevent(positions['character'][1],numberIncrement)
   directions['character'][0] = 'right'
  ## Actions
  ### Interact Action
  if console.activeKey in keymap['actionInteract']:
   queryDescType('...You can\'t interact with nothing.', 1, True)
  ### Check Action
  if console.activeKey in keymap['actionCheck']:
   queryDescType('Nothing suspicious here.', 1, True)
  ### Menu Action
  if console.activeKey in keymap['actionMenu']:
   queryDescType('This feature still needs to be worked on.', 1, False)
   queryDescType('(We don\'t know how to make this work yet.)', 2, False)
   sleep(1/tps*4)
   for row in console.descRows:
    console.descRows[row] = '> \n'
  # Reset activeKey and update positions, then wait for next tick
  console.activeKey = ''
  updatePositions()
  sleep(1/tps)

if __name__ == '__main__':
 print('Starting TheRoom...')
 print('---')
 Thread(target=loop).start()
 console.mainloop()