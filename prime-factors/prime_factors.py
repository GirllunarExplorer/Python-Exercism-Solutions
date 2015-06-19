__author__ = 'tracyrohlin'

from utils import isprime

import math

def prime_factors(number):
    prime_list =[]
    for x in xrange(2, number+1):
        while number % x == 0:
            print x
            if isprime(x):
                print "true"
                prime_list.append(x)
                number = number / x

    return prime_list

print prime_factors(7)