
def sum_of_first_n_numbers(n):
    return (n*(n+1))/2

def sum_of_squares(n):
    return (n*(n+1)*((2*n)+1))/6

print((sum_of_first_n_numbers(100))**2 - sum_of_squares(100))