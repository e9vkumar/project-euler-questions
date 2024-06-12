def letter_count(n):
    if n == 1000:
        return "onethousand",len("onethousand")
    ones = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    tens = {10:"ten",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
    special = {11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}

    ans = ""
    # div = 100

    while n > 0:
        if n >= 100:
            res = n//100
            n = n%100
            ans += ones[res] + "hundred"
            if n>0:
                ans += "and"
            continue

        if n >= 10:
            if n in tens:
                ans += tens[n]
                n=0

            else:
                if n<20:
                    ans += special[n]
                    n = 0

                else:
                    res = n//10
                    ans += tens[res*10]
                    n = n%10
            continue

        else:
            ans += ones[n]
            n = 0

    return ans,len(ans)

sum = 0
for i in range(1,1001):
    ans,s = letter_count(i)
    sum += s
    # print(i,ans,sum,"---DONE")

print(sum)
