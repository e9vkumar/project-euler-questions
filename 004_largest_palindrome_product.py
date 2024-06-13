def largest_palindromic_product(n):
    max_prod = 1
    last_multiple = ((10**n)//11)*11
    for i in range(100,1000):
        for j in range(121,last_multiple,11):
            num_str = str(i*j)
            if num_str == num_str[::-1]:
                max_prod=max(max_prod,i*j)

    return max_prod


print(largest_palindromic_product(3))