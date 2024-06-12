def find_digit_sum(n):
    return sum(int(c)**5 for c in str(n))

def check_fifth_sum(n):
    return sum(i for i in range(2,n+1) if i==find_digit_sum(i))

print(check_fifth_sum(1000000))