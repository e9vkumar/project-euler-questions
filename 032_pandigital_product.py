def check_pandigital(num_str):

    if len(num_str)!=9:
        return False
    
    num_str = "".join(sorted(num_str))

    return num_str == "123456789"

def check_product(num):
    i = 1
    while i*i <= num:
        if num%i==0 and check_pandigital(str(num)+str(i)+str(num//i)):
            return True
        
        i += 1

def solve_pandigital_product():    
    sum = 0
    for i in range(1000,10000):
        if check_product(i):
            sum += i
    return sum

print(solve_pandigital_product())