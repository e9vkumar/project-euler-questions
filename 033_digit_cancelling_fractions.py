import math

def find_digit_cancelling_fractions(limit):
    num = 1
    den = 1
    for d in range(10,10**limit):
        for n in range(10,d):
            a1 = n//10
            b1 = n%10
            a2 = d//10
            b2 = d%10
    
            if(b1==a2 and (b2!=0 and a1/b2==n/d)):
                num *= n//math.gcd(n,d)
                den *= d//math.gcd(n,d)

    return den//math.gcd(num,den)

if __name__ == "__main__":
    print(find_digit_cancelling_fractions(3))

