num = 2**1000

sum = 0
while num > 0:
    rem = num%10
    num = num//10
    sum += rem

print(sum)