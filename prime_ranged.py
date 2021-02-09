start = int(input("Enter starting point: "))
stop = int(input("Enter last point: "))
for i in range(start,stop):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)
