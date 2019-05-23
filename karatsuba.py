#  Bill Armstrong
#  May 2019
#  Karatsuba Multiplication Algorithm
###########################################

#  Tried multiple methods to use string slicing to compute
#  the a,b and c,d splits however the conversions into and
#  out of int & str caused errors depending on the unknown
#  issues.  From the math module I've used divmod() method 
#  as described below.
from math import *

#  int() method is used to force type integer rather than
#  type float.
num1 = int(5678)
num2 = int(1234)

def recIntMult (x, y):

    #  Create string instances of numbers for slicing and
    #  length computations
    if x < 10 or y < 10:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        #  have to test for odd splits and then adjust otherwise
        #  calcualtion fails on a leading zero which I think is 
        #  dropped when coverting the int x into a str.
        if n % 2 != 0:
            n -= 1

        #  divmod() takes two non-complex numbers, the first
        #  being the numerator and the second being the denominator.
        #  it returns a tuple consisting of the quotient and the
        #  remainder.  For example, the next line takes 5678 and
        #  raises it to the a power of 10 equal to 1/2 the number of
        #  digits.  This has the effect of moving the decimal point
        #  to the half way point.  Those digits left of the decimal
        #  are assigned to 'a' and those to the right (the decimal)
        #  are assigned to 'b'.
        a, b = divmod(x, 10**(n/2))
        c, d = divmod(y, 10**(n/2))

        ac = recIntMult(a,c)
        bd = recIntMult(b,d)
        #  From Roughgarden, Algorithms Illuminated Part I, P 1.3.2
        ad_bc = recIntMult((a+b),(c+d)) - ac - bd

        return ac * 10**(n) + (ad_bc * 10**(n/2)) + bd

print(recIntMult(num1, num2))