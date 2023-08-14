from math import floor, log
from numpy import polynomial
from find_r import phi

def reduce(A, n, r): # reduit A dans (Z/nZ[X])/(X^r-1)
    P = A.coef
    Q = [0] * r
    l = len(P)
    for i in range (r):
        Q[i] = sum(P[k] for k in range (i, l, r)) % n
    return polynomial.Polynomial(Q)

def fast_exp(p, m, n, r): # p est un polynome, et la fonction calcule p^m dans (Z/nZ[X])/(X^r-1)
    if m == 0: 
        return polynomial.Polynomial([1] + [0] * (r - 1))
    q = fast_exp(p, m//2, n, r)
    q1 = reduce(q**2, n, r)
    if m%2 == 0: 
        return q1
    return reduce(q1*p, n, r)

def step5(n, r): # renvoie True si (X + a)^n = X^n + a dans (Z/nZ[X])/(X^r-1) pour tout a entre 1 et l, et False sinon
    l = floor(phi(r)**0.5*log(n)/log(2))
    for a in range (1, l + 1):
        if fast_exp(reduce(polynomial.Polynomial([a, 1]), n, r), n, n, r) != reduce(polynomial.Polynomial([a] + [0] * (n - 1) + [1]), n, r):
            return False
    return True