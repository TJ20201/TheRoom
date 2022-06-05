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
 'moveRight': ['d', 'Right']
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
  if console.activeKey in keymap['moveUp']: 
   positions['character'][0]=checkPrevent(positions['character'][0],letterDecrement)
   directions['character'][0] = 'up'
  if console.activeKey in keymap['moveDown']: 
   positions['character'][0]=checkPrevent(positions['character'][0],letterIncrement)
   directions['character'][0] = 'down'
  if console.activeKey in keymap['moveLeft']: 
   positions['character'][1]=checkPrevent(positions['character'][1],numberDecrement)
   directions['character'][0] = 'left'
  if console.activeKey in keymap['moveRight']: 
   positions['character'][1]=checkPrevent(positions['character'][1],numberIncrement)
   directions['character'][0] = 'right'
  console.activeKey = ''
  updatePositions()
  sleep(1/tps)

if __name__ == '__main__':
 print('Starting TheRoom...')
 print('---')
 Thread(target=loop).start()
 console.mainloop()