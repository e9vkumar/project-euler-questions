def find_largest_prime(n):
    max_factor = 2

    while max_factor*max_factor <= n:
        while n% max_factor == 0:
            n //= max_factor
            if n==1:
                return max_factor
        max_factor += 1

    return n

print(find_largest_prime(600851475143))