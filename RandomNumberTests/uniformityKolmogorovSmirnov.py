#!/usr/bin/env python3

randnum = [float(x) for x in input("Enter list of numbers seprated by spaces:  ").split()]

HNull = "Data are a sample from a uniform distribution"

print ("\nSTEP 1: Rank the data from smallest to largest")
randnum.sort()
print ("\t%s" % str(randnum))

print ("\nSTEP 2: Compute D+ & D-")
i = 0
N = len(randnum)
dPList = []
dMList = []
for x in randnum:
    i = i + 1
    dPList.append(i / N - x)
    dMList.append(x - (i - 1) / N)

dP = max(dPList)
dM = max(dMList)
print ("\tD+ = %f" % dP)
print ("\tD- = %f" % dM)

print ("\nSTEP 3: Compute D")
d = max(dP, dM)
print ("\tD = %f" % d)

print ("\nSTEP 4: Determine the critical value, D(alpha)")
print("\tEnter Critical value for some significance level 'alpha' and sample size %d," % N)
dAplha = float(input("\tD(alpha) = "))

print ("\nSTEP 5: Compare D(alpha) & D")
if d > dAplha:
    print("\tThe null hypothesis,\n\tie. %s is rejected." % HNull)
else:
    print("\tNo evicence to reject null hypothesis,\n\tie. %s." % HNull)
