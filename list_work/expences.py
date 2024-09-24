expences=[12000,2300,1000,5200,63000,4600,12000,300]

# find count of objects in expences

expence_count=len(expences)

# print(expence_count)

# print all expences

# for i in range (0,expence_count):
#     print(expences[i])

# print expences>15000

for i in range (0,expence_count):
    if expences[i]>1500:
        print(expences[i])

# print total expence

total_expence=0

for i in range(0,len(expences)):

    total_expence=total_expence+expences[i]

print(total_expence) 

# avg expence

total_expence=0

for i in range(0,expence_count):

    total_expence=total_expence+expences[i]

    avg_expence=total_expence/len(expences)

print(avg_expence)    



