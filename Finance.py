Loaned = float(input("Please enter the amount you want to finance:\n"))
Time = int(input("Please enter the maximum amount of time in months:\n"))
APR = float(input("Please enter the APR (e.g., 6 for 6%): "))
Payment = float(input("Enter how much you want to pay per month (e.g., 500): "))
PrincipalTarget = float(input("Enter your desired principal threshold (e.g., 300): "))

# Convert APR to monthly rate
APR *= 0.01
APR /= 12

month = 1
balance = Loaned
principal_target_month = None

# Fixed minimum monthly payment
PMT = Loaned * (APR * (1 + APR)**Time) / ((1 + APR)**Time - 1)
bill = round(PMT, 2)

print("\n--- Fixed Payment Amortization Table ---")
for time in range(Time, 0, -1):
    interest = balance * APR
    principal = bill - interest
    balance -= principal

    if principal_target_month is None and principal >= PrincipalTarget:
        principal_target_month = month

    print(f"Month {month}: Payment=${bill:.2f}, Interest=${interest:.2f}, Principal=${principal:.2f}, Balance=${balance:.2f}")
    month += 1

# Total paid with interest (assuming fixed payments)
Total = round(bill * Time, 2)
int_paid = round(Total - Loaned, 2)

print("\nTotal paid and total interest: $", Total, "\n$", int_paid)

if principal_target_month:
    print(f"\n Principal portion of payment reaches at least ${PrincipalTarget:.2f} in month {principal_target_month}")
else:
    print(f"\n Principal portion never reaches ${PrincipalTarget:.2f} within the loan term.")


# ============================
# Function to calculate custom payoff time
# ============================
def calculate_payoff_months(balance, monthly_payment, apr):
    month = 1
    total_interest = 0.0
    while balance > 0:
        interest = balance * apr
        principal = monthly_payment - interest

        if principal <= 0:
            print("\n Your monthly payment is too low to pay off the interest. The loan will never be paid off.")
            return

        balance -= principal
        total_interest += interest
        month += 1

    print(f"\n With a monthly payment of ${monthly_payment:.2f}, the loan will be fully paid off in {month - 1} months.")
    print(f" Total interest paid in this case: ${round(total_interest, 2)}")

# Run the function using user's Payment input
calculate_payoff_months(Loaned, Payment, APR)
