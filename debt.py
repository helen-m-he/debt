
balance = input("Enter balance: ") # TEST 999999
annualInterestRate = input("Enter annual interest rate: ") #TEST 0.18 = 18% ANNUAL


# Store inputted balance (bc will be changing "balance" later, so need to save somewhere to later reset)
inputtedBalance = balance

# Define monthly interest rate + initial guess bounds
monthlyInterestRate = annualInterestRate/12.0
low = balance/12 #min possible monthly payment (lower bound) -- given in prompt
high = (balance*(1+monthlyInterestRate)**12)/12.0 #max possible monthly payment (upper bound) -- given in prompt


# Bisection Search
while abs(balance) > 0.001: # keep going till balance gets *close enough* to 0

    payment = (low+high)/2 # test the average of possible range
    balance = inputtedBalance # Reset balance to the inputted balance value

    # Calculate remaining balance after a year, if paying "payment" monthly
    for i in range(12):
        unpaidBalance = balance - payment
        monthlyInterestPayment = monthlyInterestRate*unpaidBalance
        balance = unpaidBalance + monthlyInterestPayment # the remaining balance at the end of each month

    # By the end of ^, "balance" = *remaining* balance after paying "payment" monthly for the whole year (goal is to get this close to 0)

    if balance > 0: # if remaining balance too high (aka balance still left; aka payment is too low), raise the lower bound
        low = payment
    if balance < 0: # if remaining balance too low (aka paid too much; aka payment is too high), lower the upper bound
        high = payment

# Print lowest FIXED monthly payment to pay off debt in one year
print("Lowest Payment: " + str(round(payment,2)))