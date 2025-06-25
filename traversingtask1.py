temp = []
total = 0
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for index in range(7):
    new = int(input("what is " + days[index] + " temerature?"))
    temp.append(new)
    total += temp[index]
total = total / 7
print("the average temprature of the week was", (total), "degrees Celsius.")