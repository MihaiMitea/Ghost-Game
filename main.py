from random import randint

print('Ghost game')

feeling_brave = True
game_on = True
score = 0

while game_on:
  while feeling_brave:
    
    # The door behind which is a ghost will be randomly selected by randint
    ghost_door = randint(1, 3)
    
    print('Three doors ahead...')
    print('A ghost behind one.')
    print('Which door do you open?')
    
    door = input('1, 2, or 3?')
    door_num = int(door)
    
    if door_num == ghost_door:
      print('GHOST!')
      feeling_brave = False
    else:
      print('No ghost!')
      print('You enter the next room.')
      score += 1
      
  print('Run away!')
  print('Game over! You scored', score)
  print('Retry?')
  
  choice = input('y/n')
  
  while choice != 'y' and choice != 'n':
    print('Invalid choice!')
    choice = input('y/n')
  
  if choice == 'n':
    print('Quitting game...')
    game_on = False
  else:
    feeling_brave = True
    pass
  
    
