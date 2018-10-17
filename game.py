#this is Rock, Paper and Scissors Game. 
#!/bin/python3

from random import randint

def determine_winner (a,b):
  if player == computer:
    winner = 'none'
  elif a == 'r' and b == 's':
    winner = 'You'
  elif a == 's' and b =='r':
    winner = 'Computer'
  elif a == 'p' and b == 'r':
    winner = 'You'
  elif a == 'r' and b == 'p':
    winner = 'Computer'
  elif a == 's' and b == 'p':
    winner = 'You'
  elif a == 'p' and b =='s':
    winner = 'Computer'
  return winner

def print_result(result):
  if result == 'none':
    print('DRAW!')
  elif result == 'You':
    print('Congratulations! You Won!')
  elif result == 'Computer':
    print ('Alas! Computer Won!')
  return


player = input ('Rock (r), or Paper(p), or Siccor(s):')

print (player, 'vs', end=' ')

chosen = randint (1,3)

if chosen == 1: # 1 is Rock
  computer = 'r'
elif chosen == 2: # 2 is Paper
  computer = 'p'
else:  # 3 is Siccor 
  computer = 's'

print (computer)

print_result(determine_winner (player, computer))