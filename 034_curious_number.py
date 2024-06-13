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


def get_digit_sum(num):
    digit_sum = sum(factorial(int(i)) for i in str(num))

    return digit_sum

def get_curious_number_sum():
    sum = 0

    for i in range(10,1000000):
        dig_sum = get_digit_sum(i)
        if i == dig_sum:
            sum += i

    return sum

print(get_curious_number_sum())