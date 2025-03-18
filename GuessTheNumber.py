import random

number = random.randint(0, 1000)

while True:
  try:
    guess = int(input('Guess a number that is between 0 and 1000: '))

    if guess < number:
      print('The number is too low. Please try again!')
    elif guess > number:
      print('The number is too high. Please try again!')
    else:
      print('Congratulations! That is the right number!')
      break
  except ValueError:
    print('Please enter a real number.')
