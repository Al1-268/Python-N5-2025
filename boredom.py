import time
import random

def loading_screen():
    print("Loading", end="")
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

hi = input("type in hi: ")

time.sleep(1)
while hi != "hi":
    loading_screen()
    time.sleep(1)
    print("you faied")
    time.sleep(1)
    print("try again")
    hi = input("type in hi: ")
loading_screen()
print("you did it")
time.sleep(1)
print("helllooooooooooooooooooo")
time.sleep(2)
print("would you like to access the calculator (y/n)")
time.sleep(1)
calculator = input("")
if calculator == "y":
    print("OK there are a few options")
    time.sleep(1)
    print("thefirst input is the first number")
    time.sleep(2)
    print ("the second input is the symbol")
    time.sleep(2)
    print("the third input is the second number")
    time.sleep(2)
    print("+ is addition")
    time.sleep(0.5)
    print("- is subtraction")
    time.sleep(0.5)
    print("* is multiplication")
    time.sleep(0.5)
    print("/ is division")
    time.sleep(0.5)
    print("now lets get started")
    time.sleep(1)
    num1 = float(input("Enter first number: "))
    symbol = input("Enter symbol: ")
    num2 = float(input("Enter second number: "))
    if symbol == "+":
        print(num1 + num2)
    elif symbol == "-":
        print(num1 - num2)
    elif symbol == "*":
        print(num1 * num2)
    elif symbol == "/":
        print(num1 / num2)
    else:
        print("invalid symbol")
else:
    print("ok")
    time.sleep(1)
    print("goodbye")
    time.sleep(1)
    print("have a nice day")
    time.sleep(1)
    print("goodbye") 
