english = int (input("Enter your English score: ")) #integer    
maths = int(input("Enter your Maths score: "))  #integer
computing = int(input("Enter your Computing score: ")) #integer
art = int(input("Enter your Art score: ")) #integer
total = english + maths + computing + art
Avg = total / 4
print("Your total score is: " + str(total),"%") #string
print("Your average score is: " + str(Avg),"%") #string