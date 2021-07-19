print("===================Welcome to the computer store===================")
print("We have many different types of computers.")
mac = 30000
dell = 20000
lowend = 10000
midend = 25000
highend = 50000

tax = 13
mactax = mac*13/100
delltax = dell*13/100
lowpc = lowend*13/100
midpc = midend*13/100
highpc = highend*13/100
print("Here are the prices of them and the tax rate is " ,tax)
print("1. Mac Prices " ,mac , " and the tax rate is " ,mactax )
print("2. Dell Prices " ,dell , " and the tax rate is " ,delltax)
print("3. Low End Desktop Prices " ,lowend, " and the tax rate is " ,lowend)
print("4. Mid End Desktop Prices " ,midend, " and the tax rate is ",midend)
print("5. High End Desktop Prices " ,highend, " and the tax rate is ",highend)

i = int(input("Now, please enter a number between 1 to 5 to buy a computer or 6."))
if i == 1:
    l = input("Now, we need your location, to deliver your order.")
    print("Now, your mac will be delivered to " ,l ," in 1-5 days.")-+
elif i == 2:
    l = input("Now, we need your location, to deliver your order.")
    print("Your dell will be delivered to " ,l ," in 2-6 days.")
elif i == 3:
    l = input("Now, we need your location, to deliver your order.")
    print("Now, your low end computer will be delivered to " ,l ," in 2-6 days.")
elif i == 4:
    l = input("Now, we need your location, to deliver your order.")
    print("Now, your mid end computer will be delivered to " ,l ," in 3-7 days.")
elif i == 5:
    l = input("Now, we need your location, to deliver your order.")
    print("Now, your high end computer will be delivered to " ,l ," in 3-7 days.")
elif i ==6:
    print("Canceling the order......")
elif i > 6:
    print("Invalid input.")


