def find():
    target = 1000
    
    for a in range(1,target+1):
        for b in range(a+1,target+1):
            c = target - a - b
            if a**2 + b**2 == c**2:
                return a*b*c
            
print(find())