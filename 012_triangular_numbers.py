import math

def num_divisors(num):
    if num < 2:
        return 1
    count = 2

    for i in range(2,int(num**(1/2))+1):
        if num%i ==0:
            count += 2

    if math.floor(math.sqrt(num)) == math.ceil(math.sqrt(num)):
        count += 1
    

    return count

def find_fact():

    fact = 0
    divs = 2
    i = 1
    while divs <= 500:
        fact = fact+i
        i += 1
        divs = num_divisors(fact)

    return fact

print(find_fact())