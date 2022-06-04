from console import Console
from threading import Thread
from time import sleep

console = Console()
def loop():
 while True:
  print(console.activeKey) if console.activeKey != '' else ''
  console.activeKey = ''
  console.activeKey
  sleep(1/20)

if __name__ == '__main__':
 print('Starting TheRoom...')
 Thread(target=loop).start()
 print('TheRoom default loop started successfully.')
 console.mainloop()