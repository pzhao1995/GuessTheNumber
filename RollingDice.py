import random

while True:
  choice = input('Would you like to roll the dice? (y/n): ').lower()
  if choice == 'y':
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      print(f'({die1}, {die2})')
  elif choice == 'n':
      print('Thanks for playing! See you next time!')
      break
  else:
      print('Invalid choice!')