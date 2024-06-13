import math
from collections import defaultdict

def is_square(n):
    return math.floor(math.sqrt(n)) == math.ceil(math.sqrt(n))

def calculate_ans(limit):
    ans = defaultdict(int)
    for a in range(2,limit+1):
        for b in range(a+1,limit+1):
            c2 = a*a + b*b
            if is_square(c2):
                c = int(math.sqrt(c2))
                if a+b+c <= limit:
                    ans[a+b+c] += 1

    return max(ans,key=ans.get)

print(calculate_ans(1000))
