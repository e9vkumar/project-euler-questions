def distinct_powers(n):
    distinct = set()
    for a in range(2,n+1):
        for b in range(2,n+1):
            distinct.add(a**b)

    return len(distinct)

print(distinct_powers(100))