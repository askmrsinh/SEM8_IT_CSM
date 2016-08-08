#!/usr/bin/env python3

from itertools import groupby
from operator import itemgetter

HNull = "Data in sample are independent"

randnum = [float(x) for x in input("Enter list of numbers seprated by spaces:  ").split()]

print ("\nSTEP 1: Count Runs up and down")
i = 0
n = []
while i < (len(randnum)-1):
  if randnum[i+1] == randnum[i]:
    n.append("o")
  elif randnum[i+1] > randnum[i]:
    n.append("+")
  elif randnum[i+1] < randnum[i]:
    n.append("-")
  i = i+1

print ("\t" + str(n))

totalRuns=0
for k,v in groupby(enumerate(n),key=itemgetter(1)):
  if k != 'o':
    v = list(v)
    print("\tRun#%d: %s" % (totalRuns+1,str(v)))
    totalRuns += 1

print ("\tObserved number of Runs is %d" % totalRuns)

n1 = n.count("+")
n2 = n.count("-")
print ("\tNumber of '+', n1=" + str(n1))
print ("\tNumber of '-', n2=" + str(n2))

print ("\nSTEP 2: Calcuate Z")
mean=(2*len(randnum)-1)/float(3)
deviation=((16*len(randnum)-29)/float(90))**(1/2)

print("\tMean = %f, Deviation = %f" % (mean, deviation))
z0=(totalRuns-mean)/deviation
print ("\tZ0 = %f" % z0)

print ("\nSTEP 3: Determine the critical value, Z(a)")
za=float(input("\tEnter Critical value for some significance level 'alpha': "))

print ("\nSTEP 4: Check if Z lies between -Z(a) & Z(a)")
if (z0 >= -za) and (z0 <= za):
  print("\tNo evicence to reject null hypothesis,\n\tie. %s." % HNull)
else:
  print("\tThe null hypothesis,\n\tie. %s is rejected." % HNull)
