#!/usr/bin/env python

import sys

m = 2147483648 # 0 < m, modulus
a = 214013 # 0 < a < m, multiplier
c = 2531011 #0 <= c < m, increment
xi = int(input("Enter a seed number for the LCG: "))

if ((xi > m) or (xi < 0)):
  sys.exit("Seed number can't be " + str(xi))

quantity = int(input("How many random numbers do you want? "))
print "\nThe Random Numbers are:"

for i in range(quantity):
  xi = (a * xi + c) % m
  print xi
