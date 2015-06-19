__author__ = 'tracyrohlin'

def slices(series, n):
    if len(series) < n:
        raise ValueError("You need a bigger list!")
    elif n <=0:
        raise ValueError("Your slice length is not big enough!")

    result = []
    for i in xrange(len(series)):
        result.append(series[i:i+n])

    result = [list(item) for item in result if len(item) == n]

    for sublist in result:
        for i in range(len(sublist)):
            sublist[i] = int(sublist[i])
    return result

print slices("97867564", 2)