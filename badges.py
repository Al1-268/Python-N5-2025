total = int(input('how much badges do you want buy'))
tickets = float(0.25)

if total >= 150:
    cost = float(total*tickets)
    tax = float(cost*0.1)
    print('your total is £',(float(cost-tax)))
else:
    if total < 150:
        print(float(total*tickets))
        