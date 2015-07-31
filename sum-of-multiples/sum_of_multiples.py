__author__ = 'tracyrohlin'

def sum_of_multiples(n, factors=[3,5]):
    factors = [f for f in factors if f > 0]
    ints = reversed(range(1,n))
    result = []
    for i in ints:
        for n in factors:
            if i%n ==0:
                result.append(i)
                break

    return sum(result)

print sum_of_multiples(10, [0])