diag_sum = 1
gap = 2
limit = 1001*1001
curr = 3
iter = 1
while curr <= limit:
    diag_sum += curr
    curr += gap
    iter += 1
    if iter == 4:
        iter = 0
        gap += 2
print(diag_sum)