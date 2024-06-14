def get_nth_permutation(num,input_str):
    num -= 1
    input_str = list(input_str)
    n = len(input_str)

    s = []
    res = ""
    for i in range(1,n+1):
        s.append(num%i)
        num = num//i

    for i in reversed(s):
        res += input_str[i]
        input_str.pop(i)

    return res

print(get_nth_permutation(10**6,"0123456789"))