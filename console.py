    ### #################################################### ###  
 ####                                                          ####
#   The Console for The Room. Contains multiple elements such as   #
#   the map, the interactions and descriptions.                    #
 ####                                                          ####
    ### #################################################### ###  

from tkinter import Tk, Label
font = ("Consolas", 20)
labelConfig = {'anchor':'w'}
isDebug = __name__ == "__main__"
bg = '#111111'

class Console(Tk):
 def __init__(self, title='TheRoom Console'):
  super().__init__()
  # Configuration #
  self.config(background=bg)
  self.geometry('750x490')
  self.title(title)
  self.mapRows = mr = {
    '0': '  12345678\n',
  	'a': 'A ########\n',
  	'b': 'B #      #\n',
  	'c': 'C #      #\n',
  	'd': 'D #      #\n',
  	'e': 'E ########\n'
  }
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
  self.map.place(x=0,y=0,width=160,height=190)
  ## Description Element ##
  self.desc = Label(foreground='#ffffff',background=bg if isDebug == False else '#00ff00',  font=font)
  self.desc.config(**labelConfig)
  self.desc.place(x=0,y=215,width=750,height=150)
  ## Interaction Element ##
  self.actLabl = Label(foreground='#ffffff',background=bg if isDebug == False else '#0000ff',font=font)
  self.actLabl.config(**labelConfig)
  self.actLabl.place(x=0,y=390,width=375,height=100)
  self.updateElements()
  # Loop #
  self.mainloop()
  
 def updateElements(self):
  mr,dr,ar = self.mapRows,self.descRows,self.actRows
  self.actLabl.config(text='\n'+ar['1']+ar['2']+ar['3'])
  self.desc.config(text='\n'+dr['1']+dr['2']+dr['3']+dr['4']+dr['5'])
  self.map.config(text='\n'+mr['0']+mr['a']+mr['b']+mr['c']+mr['d']+mr['e'])

# Run standalone on Debug #
if isDebug:
 console = Console()
