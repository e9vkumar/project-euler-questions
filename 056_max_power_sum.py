def find_digit_sum(n):
    return sum(int(c) for c in str(n))

def find_powers(limit):
    max_sum = 0
    for a in range(1,limit):
        for b in range(1,limit):
            max_sum = max(max_sum,find_digit_sum(a**b))

    return max_sum

print(find_powers(100))