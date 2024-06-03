import os
import time

def loader(time_delay=0.05) -> None:
    os.system('clear')
    
    completed = 0
    progress:list[str] = ['#']
    
    for i in range(0, 31):
      if i > 0:
         completed += 100//30
      progress.insert(1, '#')
      print('|==================================|')
      print(f"{completed}%", "".join(progress))
      print('|==================================|\n')

      time.sleep(time_delay)
      os.system('clear')

# Test the loader
if __name__ == '__main__':
    loader()