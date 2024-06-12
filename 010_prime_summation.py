def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2

    while p*p <= n:
        if(prime[p]):
            for i in range(p*p,n+1,p):
                prime[i] = False
        p += 1
    # print(prime)
    return sum(i for i in range(2,n+1) if prime[i])


print(sieve_of_eratosthenes(2*(10**6)))