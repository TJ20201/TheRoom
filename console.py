    ### #################################################### ###  
 ####                                                          ####
#   The Console for The Room. Contains multiple elements such as   #
#   the map, the interactions and descriptions.                    #
 ####                                                          ####
    ### #################################################### ###  

from tkinter import Tk, Label
font = ("Consolas", 20)
half_font = ("Consolas", 10)
labelConfig = {'anchor':'w'}
isDebug = False
isSelfRunnable = __name__ == "__main__"
bg = '#111111'

class Console(Tk):
 def __init__(self, title='TheRoom Console', debugMode=False):
  super().__init__()
  # Configuration #
  self.config(background=bg)
  self.geometry('750x490')
  self.title(title)
  self.bind('<Key>',self.key_pressed)
  self.activeKey = ''
  isDebug = debugMode
  self.mapRows = mr = {
    '0': '  1 2 3 4 5\n',
  	'a': 'A ╭───────╮\n',
  	'b': 'B │       │\n',
  	'c': 'C │       │\n',
  	'd': 'D │       │\n',
  	'e': 'E ╰───────╯\n'
  }
  self.mapKeyRows = mkr = ''.join([
    '  ┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓\n',
    '  ┃  Symbol   ┃        Key       ┃\n',
    '  ┣━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━┫\n',
    '  ┃     x     ┃    The Player    ┃\n',
    '  ┃     #     ┃     An object    ┃\n',
    '  ┃           ┃                  ┃\n',
    '  ┃           ┃                  ┃\n',
    '  ┃           ┃                  ┃\n',
    '  ┃           ┃                  ┃\n',
    '  ┃           ┃                  ┃\n',
    '  ┃           ┃                  ┃\n',
    '  ┗━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛\n'
  ])
  self.descRows = dr = {
  	'1': '> \n',
  	'2': '> \n',
  	'3': '> \n',
  	'4': '> \n',
  	'5': '> \n'
  }
  self.actRows = ar = {
  	'1': '    1: Interact\n',
  	'2': ' 2: Check\n',
  	'3': '3: Menu\n'
  }
  # Elements #
  ## Map Element ##
  self.map = Label(foreground='#ffffff', background=bg if isDebug == False else '#ff0000',font=font)
  self.map.config(**labelConfig)
  self.map.place(x=0,y=0,width=190,height=190)
  ## Description Element ##
  self.desc = Label(foreground='#ffffff',background=bg if isDebug == False else '#00ff00',  font=font)
  self.desc.config(**labelConfig)
  self.desc.place(x=0,y=215,width=750,height=150)
  ## Interaction Element ##
  self.actLabl = Label(foreground='#ffffff',background=bg if isDebug == False else '#0000ff',font=font)
  self.actLabl.config(**labelConfig)
  self.actLabl.place(x=-60,y=390,width=435,height=100)
  ## Map Key Element ##
  self.mkey = Label(foreground='#ffffff' if isDebug == False else '#000000',background=bg if isDebug == False else '#ffff00',font=half_font)
  self.mkey.config(anchor='nw')
  self.mkey.place(x=215,y=0,width=535,height=190)
  self.updateElements()

 def updateElements(self):
  mr,dr,ar,mkr = self.mapRows,self.descRows,self.actRows,self.mapKeyRows
  self.mkey.config(text=mkr)
  self.actLabl.config(text='\n'+ar['1']+ar['2']+ar['3'])
  self.desc.config(text='\n'+dr['1']+dr['2']+dr['3']+dr['4']+dr['5'])
  self.map.config(text='\n'+mr['0']+mr['a']+mr['b']+mr['c']+mr['d']+mr['e'])

 def key_pressed(self, event):
  self.activeKey = event.keysym
  if isDebug: print(event.char, self.activeKey)

# Run standalone if possible #
if isSelfRunnable:
 console = Console()
