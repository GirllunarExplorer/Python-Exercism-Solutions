__author__ = 'tracyrohlin'
from math import ceil, sqrt

def prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in xrange(2, int(ceil(sqrt(n))) + 1):
            if n % i == 0:
                return False

    return True

def sieve(n):
    number_list = [i for i in xrange(2, n+1) if prime(i)]
    return number_list