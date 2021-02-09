p = float(input("Enter the principle amount : "))
r = float(input("Enter the rate : "))
t = int(input("Enter the time: "))
a = p * (pow((1 + r / 100), t))
ci = a-p
print("compound interest is : ", ci)
