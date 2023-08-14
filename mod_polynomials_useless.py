import cmath
from math import floor, log
from find_r import phi

def reduce(P, n, r): # reduit P dans (Z/nZ[X])/(X^r-1)
    Q = [0] * r
    l = len(P)
    for i in range (r):
        Q[i] = sum(P[k] for k in range (i, l, r)) % n
    return Q

def FFT(a, signe = 1):
    n = len(a)
    if n == 1:
        return a
    else:
        a1, a2 = a[::2], a[1::2]
        b1, b2 = FFT(a1, signe), FFT(a2, signe)
        y = [0] * n
        wn = cmath.exp(signe * 2j * cmath.pi / n)
        w = 1
        for k in range(n // 2):
            y[k] = b1[k] + w * b2[k]
            y[k + n // 2] = b1[k] - w * b2[k]
            w *= wn
        return y
        
def IFFT(a):
    b = FFT(a, -1)
    n = len(a)
    return [round(x.real / n) for x in b]
    
def multFFT(a, b): # j'imagine qu'il faut que les deux polynomes soient de même taille quitte à rajouter des zeros
    n = len(a)
    k = 1
    while k // 2 < n:
        k = 2 * k
    a = a + ([0] * (k - n))
    b = b + ([0] * (k - n))
    ffta = FFT(a, 1)
    fftb = FFT(b, 1)
    fftc = [ffta[i] * fftb[i] for i in range(k)]
    c = IFFT(fftc)
    return c
    
def fast_exp(p, m, n): # p est un tableau de taille r, et la fonction calcule p^m dans (Z/nZ[X])/(X^r-1)
    r = len(p)
    if m == 0: 
        return [1] + [0] * (r - 1)
    q = fast_exp(p, m//2, n)
    q1 = reduce(multFFT(q, q), n, r)
    if m%2 == 0: 
        return q1
    return reduce(multFFT(q1, p), n, r)

def step5(n, r): # renvoie True si (X + a)^n = X^n + a dans (Z/nZ[X])/(X^r-1) pour tout a entre 1 et l, et False sinon
    l = floor(phi(r)**0.5*log(n)/log(2))
    for a in range (1, l + 1):
        if fast_exp(reduce([a, 1], n, r), n, n) != reduce([a] + [0] * (n - 1) + [1], n, r):
            return False
    return True