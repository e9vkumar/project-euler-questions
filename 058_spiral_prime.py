import math

prime = []

def is_prime(n):

    if n in prime:
        return True

    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    prime.append(n)
    return True



gap = 2
prime_count = 1
start = 3
iter = 1
while (prime_count/(gap+gap+1)) >= 0.1 :
    start += gap
    iter += 1
    if is_prime(start):
        prime_count += 1
    if iter == 4:
        iter = 0
        gap += 2

print(gap+1)
