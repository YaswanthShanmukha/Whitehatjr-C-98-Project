lower = int(input("Enter the lower range limit : "))
upper = int(input("Enter the upper range limit : "))
num = int(input("Enter the number to be divided by : "))

for i in range(lower,upper+1):
    if(i%num == 0):
        print(i)