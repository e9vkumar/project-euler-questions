from collections import defaultdict

dp = defaultdict(int)
def sum_divisors(num):
    if dp[num] != 0:
        return dp[num]
    sum = 1

    for i in range(2,int(num**(1/2)+1)):
        if num % i ==0:
            sum += i
            sum += num//i
    dp[num]=sum
    return sum

sum = 0

for i in range(6,10000):
    if sum_divisors(sum_divisors(i)) == i and sum_divisors(i)!=i:
        sum += i

print(sum)