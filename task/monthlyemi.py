# write a program to calculate 
    #monthly emi
    #total intrest payable- loan amount-total payment
    # total payment-loan amount *n

loan_amount=int(input("enter amount"))

intrest_rate=int(input("enter intrest rate"))

tenure=int(input("enter years"))

#EMI= p*r*(r+1)^n/(1+r)^n-1

r=monthly_intrest_rate=intrest_rate/12/100

n=tenure*12

one_pluse=(r+1)**n

EMI=(loan_amount*r*one_pluse)/(one_pluse-1)

print(f"{EMI} is the monthly EMI amount")

total_payable_amount=EMI*n

print(f"{total_payable_amount} is taotal payment amount ")

intrest_payed=total_payable_amount-loan_amount
print(f"{intrest_payed} amount payed as intrest")
