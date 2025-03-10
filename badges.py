total = int(input('how much badges do you want buy'))
badge = float(0.25)

if total >= 150:
    cost = float(total*badge)
    discount = float(cost*0.1)
    print('your total is £',(float(cost-discount)))
else:
    if total < 150:
        print(float(total*badge))
        