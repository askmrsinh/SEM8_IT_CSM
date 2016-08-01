#!/usr/bin/env python2

import math


choice = int(input(\
"""Random Variate Generation using:
	[1] Exponential distribution
	[2] Uniform distribution
	[3] Weibull distribution
	[4] Triangular distribution

	Enter choice: """))

if choice == 1:
    print "\n\nExponential distribution"
    lamd = float(input("  lamda="))
    ri = float(input("  ri="))
    xi = (-1) * math.log(1-ri) / lamd

elif choice == 2:
    print "\n\nUniform distribution"
    a = float(input("  a="))
    b = float(input("  b="))
    ri = float(input("  ri="))
    xi = a+(b-a) * ri

elif choice == 3:
    print "\n\nWeibull distribution"
    alpha = float(input("  alpha="))
    beta = float(input("  beta="))
    ri = float(input("  ri="))
    xi = alpha * ((-1) * math.log(1-ri)) ** (1/beta)

elif choice == 4:
    print "\n\nTriangular distribution"
    c = float(input("  c"))
    ri = float(input("  ri"))
    if ri > 0 and ri <= 1 / c:
        xi = (c * ri) ** 0.5
    else:
        xi = c - (c * (c - 1) * (1 - ri)) ** 0.5

print(str(xi))

			