__author__ = 'tracyrohlin'

from math import sqrt

def is_prime(n):
    if n%2 ==0 and n>2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_factors(number):
    prime_list =[]
    for x in range(2, number+1):
        while number % x == 0:
            if is_prime(x):
                prime_list.append(x)
                number = number / x

    return prime_list

def raindrops(n):
    j = n
    prime_facts = list(set(prime_factors(n)))
    drops = {3:"Pling", 5:"Plang", 7:"Plong"}
    storm = [drops[n] for n in prime_facts if n in drops]
    cloud = "".join(storm)
    if not cloud:
        return str(j)
    return cloud



