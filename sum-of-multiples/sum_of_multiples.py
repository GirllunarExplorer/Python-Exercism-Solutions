__author__ = 'tracyrohlin'

def sum_of_multiples(n, multiples=None):
    result = []
    if not multiples:
            multiples = [3,5]

    ints = range(1,n)
    while len(ints) > 0:
        i = ints.pop()
        for n in multiples:
            try:
                if i%n ==0:
                    result.append(i)
                    break
            except:
                result.append(0)

    return sum(result)




print sum_of_multiples(10, [0])