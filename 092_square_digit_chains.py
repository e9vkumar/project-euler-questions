from collections import defaultdict

def compute_ans(limit):
    return sum(1 for i in range(limit) if get_final_point(i)==89)

def get_final_point(num):
    while num not in [1,89]:
        num = square_digit_sum(num)
    return num

square_sums = defaultdict(int)
def square_digit_sum(num):
    if square_sums[num]!=0:
        return square_sums[num]
    ans = 0
    key = num
    while num>0:
        rem = num%10
        ans += rem**2
        num = num//10
    square_sums[key]=ans
    return ans

if __name__ == "__main__":
    print(compute_ans(10**7))