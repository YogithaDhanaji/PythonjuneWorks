# emi calculater progarm

# EMI=p*r*(1+r)**n/(1+r)**n-1

# p=> loan amount
# r=>intrest rate
# t=>tenure(years)=>months

# Set loan_amount
loan_amount=200000

#set intrest_rate
intrest_rate=9

#set tenure=10
tenure=10

#convert yearly intrest rate into monthly intrest rate

r=tenure/12/100

# convert tenute in year to months 

n=tenure_in_months=tenure*12

onePlus_r=(1+r)**n

EMI=(loan_amount*r*onePlus_r)/(onePlus_r-1)

print(EMI)

total_payable_amount=EMI*n

print(f"monthly EMI={EMI}")

print(f"total payable amount={total_payable_amount}")

totale_intrest_payable=total_payable_amount-loan_amount

print(f"Total intrest payable amount={totale_intrest_payable}")