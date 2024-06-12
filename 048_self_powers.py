def find_power_sum(n):
    sum = 0
    digit_limit = 10**10
    for i in range(1,n+1):
        sum += (i**i)%digit_limit
    return sum%digit_limit

print(find_power_sum(1000))