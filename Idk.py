import random

print("type in <hello>")
hello = input() 
    
while hello != "hello":
    print("your wrong")
    print("Try Again")
    print("type in <hello>")
    hello = input() 
print("hello!!!!!!!!")
name = input("what is your name")

arr = ["hi","hello","bonjour","Hola","Ciao","Hallo","Anyeong Haseyo"]
print(random.choice(arr),name)

arr2 = ["your a boomer","your a millenial","your a gen z","your a gen x","your a gen y"]
age = int(input("what is your age"))
if age < 18:
    print("you are a minor")
else:
    print(random.choice(arr2),name)