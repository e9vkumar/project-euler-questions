def compute_string(n):
    i = 1
    s = ""
    while len(s)<=n:
        s += str(i)
        i += 1
    return s

def compute_val(n,digits):
    res = compute_string(n)
    prod = 1
    for digit in digits:
        prod *= int(res[digit-1])
    return prod


print(compute_val(10**6,[1,10,100,1000,10000,100000,1000000]))