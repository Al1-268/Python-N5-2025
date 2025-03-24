tempratures = []
total = 0
temp = int(input("Enter temprature: "))
while temp <-20 or temp > 50:
    print("Invalid temprature")
    temp = int(input("Enter temprature: "))
else:
    for i in range (4):
        temp = int(input("Enter temprature: "))
        tempratures.append(temp)  

for x in range(len(tempratures)):
       
       total += tempratures[x]    
print('The total degrees is:' + str(round(total, 2))) 

