n = int(input("Enter a number : "))
s = 0
num =n
while(n>0):
    r = n % 10
    s = s + r* r* r
    n = n//10
if(s==num):
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")
