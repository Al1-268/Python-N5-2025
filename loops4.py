# Program 4 - Investigate and modify
import random


rightnumber = random.randint(1,1)
name = input("What is your name? ")
guess = 1
number = int(input("Guess a number: "))
while (guess < 10) and (number != rightnumber):
  print("Not right. Try again.")
  number = int(input("Guess a number: "))
  guess = guess + 1
if number == rightnumber:
  arr = ["Well done","Good job","You got it","You are a genius","You are a mastermind","You are a wizard","You are a psychic","You are a mind reader","You are a fortune teller","You are a seer","You are a"]
  print(random.choice(arr),name)