limit = 1000
prev,curr = 0,1
count = 2
while True:
    ele = prev + curr
    count += 1
    if len(str(ele)) == limit:
        break
    prev = curr
    curr = ele

print(count-1)