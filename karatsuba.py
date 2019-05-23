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
import time

#  int() method is used to force type integer rather than
#  type float.
num1 = int(567234654345678675456345822)
num2 = int(123968768797865545876587654)

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

start = time.time()
result1 = (recIntMult(num1, num2))
end = time.time()
print("karatsuba algorithm: ", result1, "  elapsed time: ", end - start)

start = time.time()
result2 = (num1 * num2)
end = time.time()
print("python algorithm: ", result2, "  elapsed time: ", end - start)

'''
After some experimenting python3.7 seems to have a better time than the 
karatsuba algorithm.  After some additional research, python3.7 implements
two seperate algorithms for its built in multiplication method.  For 
"small numbers" python uses teh O(N^2) method (long hand) while for "large
numbers" python implements the karatsuba algorithm.  Even with larger 
numbers the built in python method executes notably fast.  The reason being
that the karatsuba code is handled in C code and runs faster.  There is also
the potential (:-)) that the source python code which is compiled into C is
more effecient than the code above.
'''