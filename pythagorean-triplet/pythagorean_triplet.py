__author__ = 'tracyrohlin'

from fractions import gcd

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def is_triplet(num_tuples):
    num_list = list(num_tuples)
    a, b, c = num_list[0], num_list[1], num_list[2]
    a, b, c = a**2, b**2, c**2
    if a+b == c:
        return True
    elif a+c == b:
        return True
    elif b+c == a:
        return True
    return False

def yield_triplet(minimum, maximum):
    for a in xrange(minimum, maximum+1):
        for b in xrange(minimum+1, maximum+1):
            for c in xrange(minimum+2, maximum+1):
                if is_triplet([a,b,c]):
                    yield [a,b,c]


def triplets_in_range(minimum, maximum):
    return set([tuple(sorted(x)) for x in yield_triplet(minimum, maximum)])

def primitive_triplets(b):
    if b %4 ==0:
        ls = []
        factors_list = list(factors((b//2)))
        for m in factors_list:
            for n in factors_list:
                if (m-n) % 2 != 0 and m > n:
                    if gcd(m, n) == 1:
                        a, c = (m**2)-(n**2), (m**2)+(n**2)
                        triplet = [a, b, c]
                        triplet.sort()
                        if is_triplet(tuple(triplet)):
                            ls.append(tuple(triplet))
        return set(ls)
    else:
        raise ValueError


