from math import gcd
    
def find_r(n):
    r = 2
    while True:
        if gcd(r, n) == 1:
            k, boo, p = 1, True, n%r
            while boo and 2**(k**0.5) <= n:
                if p == 1:
                    boo = False
                p = (n*p)%r
                k += 1
            if boo: return r
        r += 1

def phi(n):
    a = 1
    for i in range (2, n):
        if gcd(n, i) == 1:
            a += 1
    return a