#!/usr/bin/env python3

total=int(input("Enter total number of three digit random numbers: "))

HNull = "Data in sample are independent"

print ("\nSTEP 1: Get observed counts")
while (True):
   obsAllDiff=int(input("\tEnter the count of numbers which have all digits different: "))
   obsAllSame=int(input("\tEnter the count of numbers which have all digits same: "))
   obsTwoSame=int(input("\tEnter the count of numbers which have two digits same: "))
   if (obsAllDiff+obsAllSame+obsTwoSame==total):
      break
   else:
      print("\t\tThe Numbers don't add up! Try again.")

print ("\nSTEP 2: Calcuate probablaities of each possibility")
pAllDiff=0.9*0.8
pAllSame=0.1*0.1
pTwoSame=1-(pAllDiff+pAllSame)
print("\tCase 1: The individual digits can be all different.")
print("\tp(AllDiff) = %f" % pAllDiff)
print("\tCase 2: The individual digits can all be the same.")
print("\tp(AllSame) = %f" % pAllSame)
print("\tCase 3: There can be one pair of like digits.")
print("\tp(TwoSame) = %f" % pTwoSame)

print ("\nSTEP 3: Calcuate expected counts")
expAllDiff=total*pAllDiff
expAllSame=total*pAllSame
expTwoSame=total*pTwoSame
print("\tExpected count of all digits different = %f" %expAllDiff)
print("\tExpected count of all digits same = %f" %expAllSame)
print("\tExpected count of two digits same = %f" %expTwoSame)

print ("\nSTEP 4: Calcuate X2")
x2AllDiff=(obsAllDiff-expAllDiff)**2/expAllDiff
x2AllSame=(obsAllSame-expAllSame)**2/expAllSame
x2TwoSame=(obsTwoSame-expTwoSame)**2/expTwoSame
x2=x2AllDiff+x2AllSame+x2TwoSame
print ("\tX2 = %f" % x2)

print ("\nSTEP 5: Determine the critical value, X(alpha)")
xAlpha=float(input("\tEnter the critical value: "))

print ("\nSTEP 6: Compare X(alpha) & X2")
if x2>xAlpha:
    print("\tThe null hypothesis,\n\tie. %s is rejected." % HNull)
else:
    print("\tNo evicence to reject null hypothesis,\n\tie. %s." % HNull)
