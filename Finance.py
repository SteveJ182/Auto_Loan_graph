Total=float(input("Please enter the amount you want to finance:\n"))
Time=int(input("Please enter the amount of time in months:\n"))
APR=float(input("Please enter the APR"))
APR/=12
APR*=0.01
month=1
for time in range(Time, 0, -1):
    
    ptp=Total/time
    bill=ptp+(Total*APR)
    print("Amount due for month ", month, ": ", bill)
    month+=1
    Total-=bill