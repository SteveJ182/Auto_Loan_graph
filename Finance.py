Loaned = float(input("Please enter the amount you want to finance:\n"))
Time = int(input("Please enter the maximum amount of time in months:\n"))
APR = float(input("Please enter the APR (e.g., 6 for 6%): "))
Payment = float(input("Enter how much you want to pay per month (e.g., 500): "))
Threshold = float(input("Enter your interest threshold (e.g., 300): "))
 # Convert from percent to decimal
APR*=0.01
APR/=12
month=1
limit = 300


#Initial Monthly Payment amount
PMT = Loaned*(APR*(1+APR)**Time) / ((1+APR) ** Time -1)
bill = round(PMT, 2)

for time in range(Time, 0, -1):
    
    print("Amount due for month ", month, ": ", bill)
    month+=1

#Total paid with interest
Total = round(bill*Time, 2)
int_paid = round(Total-Loaned, 2)

print("Total paid and total interest: $", Total, "\n$", int_paid)
