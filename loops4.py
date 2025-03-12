# Program 4 - Investigate and modify
import random

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(arr)
rightnumber = random.choice(arr)

guess = 1
number = int(input("Guess a number: "))
while (guess < 3) and (number != rightnumber):
  print("Not right. Try again.")
  number = int(input("Guess a number: "))
  guess = guess + 1
if number == rightnumber:
  print("Well done! You guessed the right number.")