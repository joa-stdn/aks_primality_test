# Around the AKS Primality Test

This repository contains a derivation of the polynomial nature of the AKS primality test,
as well as a Python implementation.

### Introduction
Up to the early 21st century, the existence of a primality test in polynomial time was an
open problem. 

Since ancient times, mathematicians have known how to determine whether a given integer
was prime in $O(\sqrt{n})$, by successively examining divisibility by integers smaller than
$\sqrt{n}$. Yet this basic algorithm has an exponential complexity in the size of the input $n$
(since $n$ is encoded in $\log(n)$ bits).

In this work, I study the AKS algorithm (named after Manindra Agrawal, Neeraj Kayal, et Nitin Saxena),
that provided in 2002 the first demonstration that the primality test problem could be
solved in polynomial time.

### Final report
The final report for this project is available in the ```pdf``` folder (in French).

### References
[1] M. Agrawal, N. Kayal, N. Saxena, *PRIMES is in P*, 2002

[2] M. Nair, *On Chebyshev-type inequalities for primes*, 1982

[3] R. Lidl, H. Niederreiter, *Introduction to finite fields and their applications*, Cambridge University Press, 1986

[4] Joachim von zur Gathen, Jürgen Gerhard, *Modern Computer Algebra*, Cambridge University Press, 1999

Ecole Normale Supérieure (Paris) Entrance Examination (Spring 2019)
