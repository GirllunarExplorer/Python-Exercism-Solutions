__author__ = 'tracyrohlin'

def slices(series, n):
    if len(series) < n:
        raise ValueError("You need a bigger list!")

    result = []
    for i in xrange(len(series)-1):
        sublist = list(map(int, series[i:i+n]))
        result.append(sublist)
    return result

def largest_product(series, n):
    if not series:
        return 1
    elif len(series) < n:
        raise ValueError
    nums = slices(series, n)
    result = []
    for n_pair in nums:
        products = reduce(lambda x, y: x*y, n_pair)
        result.append(products)
    return max(result)