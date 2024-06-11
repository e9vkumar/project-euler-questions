def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i

    return fact

def find_paths(n):
    return int(factorial(2*n)/(factorial(n)**2))

print(find_paths(20))
# a = factorial(3)
# b = factorial(6)
# print(a,b,b/(a*a))
# print(find_paths(3))

