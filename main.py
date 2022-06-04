from console import Console
from threading import Thread
from time import sleep

console = Console()
basemap = "{'0': '  12345678\\n','a': 'A ########\\n','b': 'B #      #\\n','c': 'C #      #\\n','d': 'D #      #\\n','e': 'E ########\\n'}"
curmap = console.mapRows
tps = 20

keymap = {
 'moveUp': ['w', 'Up'],
 'moveDown': ['s', 'Down'],
 'moveLeft': ['a', 'Left'],
 'moveRight': ['d', 'Right']
}

positions = {
 'characterOld': ['C', 4],
 'character': ['C', 4]
}

blocked = [
 # Wall Blocks
 ['A', '*'], ['*', 1], ['E', '*'], ['*', 8]
]
# Change * shortcut to A-E and 1-8
blockedTemp = blocked
for block in blocked:
 if block[0] == '*':
  for i in range(5):blockedTemp.append([chr(i+65), block[1]])
 if block[1] == '*':
  for i in range(7):blockedTemp.append([block[0], i+1])
del blockedTemp

def letterDecrement(char:str): return changePrevention(chr(ord(char)-1))
def letterIncrement(char:str): return changePrevention(chr(ord(char)+1))
def numberDecrement(targ:int): return changePrevention(targ-1)
def numberIncrement(targ:int): return changePrevention(targ+1)
def changePrevention(targ):
 # Out of Bounds Check
 if not targ in ['A','B','C','D','E',1,2,3,4,5,6,7,8]: return 'preventMove'
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
 curmap[charver] = curmap[charver][:charhor]+'x'+curmap[charver][charhor+1:]
 # Update Map
 console.mapRows = curmap
 console.updateElements()

def loop():
 while True:
  # Handlers
  positions['characterOld'] = eval(str(positions['character']))
  if console.activeKey in keymap['moveUp']: 
   positions['character'][0]=checkPrevent(positions['character'][0],letterDecrement)
  if console.activeKey in keymap['moveDown']: 
   positions['character'][0]=checkPrevent(positions['character'][0],letterIncrement)
  if console.activeKey in keymap['moveLeft']: 
   positions['character'][1]=checkPrevent(positions['character'][1],numberDecrement)
  if console.activeKey in keymap['moveRight']: 
   positions['character'][1]=checkPrevent(positions['character'][1],numberIncrement)
  console.activeKey = ''
  updatePositions()
  sleep(1/tps)

if __name__ == '__main__':
 print('Starting TheRoom...')
 print('---')
 Thread(target=loop).start()
 console.mainloop()