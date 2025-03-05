total = int(input('how much tickets do you want buy'))
tickets = int(10)

if total >= 3:
    cost = int(total*tickets)
    tax = int(cost*0.1)
    print('your total is £',(int(cost-tax)))
else:
    if total < 3:
        print(int(total*tickets))
        
