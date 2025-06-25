dogfood = []
total = 0

for index in range(5):
    weight = int(input("enter the weighht of the cannerd dog food in g: "))
    while weight < 0 or weight > 300:
        print("invalid weight")
        weight = int(input("enter the weighht of the cannerd dog food in g: "))
    dogfood.append(weight)
    total = total + dogfood[index]
print("the total weightof the food the dag has eaten is", total, "grams worth of canned dog food.")