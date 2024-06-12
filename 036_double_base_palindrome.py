def check_palindrome(s):
    if type(s) is not str:
        s = str(s)

    i = 0
    j = len(s) - 1
    while i<=j:
        if s[i]!=s[j]:
            return False
        i += 1
        j -= 1

    return True

print(sum(i for i in range(1,(10**6)+1) if check_palindrome(i) and check_palindrome(bin(i)[2:])))