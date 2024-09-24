# find missing +ve integer

arr=[0,1,2,3]

n=len(arr)

sum_of_n=n*(n+1)/2

current_num=sum(arr)

missing_num=sum_of_n-current_num

print(round(missing_num))
