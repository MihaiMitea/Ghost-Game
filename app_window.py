import tkinter as tk
from random import randint

class GhostGame:
  def __init__(self, root):
    # root is the main window object
    self.root = root
    self.root.title("Ghost Game")
    self.root.geometry("300x200") # Width x Height
    
    # Creates a label
    self.label = tk.Label(self.root, text="Choose a door!")
    self.label.pack(pady=20) # 'pack' puts it on the screen
      
    # A random number from 1 to 3 will represent the door behind which there lies a ghost  
    ghost_door = randint(1, 3) 
      
    # The game will show a message depending on which kind of door you chose to open  
    def room(door):
      if ghost_door == door:
         self.label.config(text="You entered the room! GHOST!", fg="red")
      else:
        self.label.config(text="You entered the room! It is safe!", fg="green")
    
     # Creates buttons
    # 'command' tells the button which function to run when clicked
    btn1 = tk.Button(root, text="Door 1", command = lambda: room(1))
    btn1.pack(side="left", padx=20, expand=True)

    btn2 = tk.Button(root, text="Door 2", command = lambda: room(2))
    btn2.pack(side="left", padx=20, expand=True)

    btn3 = tk.Button(root, text="Door 3", command = lambda: room(3))
    btn3.pack(side="left", padx=20, expand=True)
    
  
    
# Start the game
window = tk.Tk()        # Create the 'engine' for the window
app = GhostGame(window) # Pass the window into our Class
window.mainloop()       # Keep the window open