# bitwise operatores (&,|,^)

# x     y       x&y     x|y     x^y

# 0     1       0       1       1

# 0     0       0       0       0   

# 1     1       1       1       0

#1      0       0       1       1

print(1&0)

print(1&1)

print(1|1)

print(1^0)

print(1^1)

# 0=> 0000
# 1=> 0001
# 2=> 0010
# 3=> 0011
# 4=> 0100
# 5=> 0101
# 6=> 0110
# 7=> 0111
# 8=> 1000
# 9=> 1001

print(2|4)
#0010|0100
#=========


print(3&4)

#msb and lsb

# msb=> 0 +ve and 1 -ve (most significant bit)

#lsb- least significant bit

print(-1&2)

input(3&4)
print(3&4)
