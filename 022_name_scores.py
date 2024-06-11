running_total = 0
with open('data/names.txt','r') as fp:
    content = fp.readlines()
    names = content[0].strip().split(',')
    names = sorted(names)
    # print(names[937])
    for i in range(len(names)):
        s = names[i]
        score = 0
        for j in range(len(s)):
            if s[j] == '"':
                continue
            score += (ord(s[j]) - 64)
            # print(s[j],ord(s[j]) - 64)
        running_total += score*(i+1)
        if i==937:
            print(score,i+1,running_total)
print(running_total)