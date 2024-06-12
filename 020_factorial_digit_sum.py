def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def sum_digits(n):
    s = str(n)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    return sum

n = 100
print(factorial(n))
print(sum_digits(factorial(n)))