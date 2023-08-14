def perfect_pow(n): # Renvoie True si et seulement si n=1 ou si n est une puissance parfaite
    if n == 1: return True
    b = 2
    while 2**b <= n:
        x, y = 1, n + 1
        while y - x > 1:
            a = (x + y) // 2
            if a**b > n:
                y = a
            else:
                x = a
        if x**b == n:
            return True
        b += 1
    return False