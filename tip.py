print("Welcome to tip claculator!")
bill=float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

pay = bill * (1+tip/100)
each_pay = pay/people

each2_pay = "{:.2f}".format(each_pay)
print(each2_pay)