from time import clock
from perfect_pow import perfect_pow
from find_r import find_r
from mod_polynomials_2 import step5

def temps(f, arg):
    t = clock()
    f(arg)
    return (clock() - t)

def aks(n):
    if perfect_pow(n): return False
    r = find_r(n)
    for a in range (2, r + 1):
        d = pgcd(a, n)
        if d > 1 and d < n:
            return False
    if n <= r: return True
    return step5(n, r)