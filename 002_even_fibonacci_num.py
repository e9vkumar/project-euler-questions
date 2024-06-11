limit = 4_000_000
fib = [1,2]
i = 2
ele = 3
sum = 2
while ele <= limit:
    ele = fib[i-1] + fib[i-2]
    fib.append(ele)
    if ele%2 == 0:
        sum += ele
    i += 1

print(sum)