factorials = [1,1]
def factorial(n):
    stored = len(factorials) 
    if  stored<n+1:
        fact = factorials[-1]
        for i in range(stored,n+1):
            fact = fact*i
            factorials.append(fact)
    
    else:
        return factorials[n]
        

    return fact


def ncr(n,r):
    return (factorials[n])/(factorials[n-r]*factorials[r])

def find_selections(limit):
    factorial(limit)
    count = 0
    for n in range(1,limit+1):
        for r in range(1,n+1):
            if ncr(n,r) > 10**6:
                count += 1

    return count

print(find_selections(100))