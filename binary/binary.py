__author__ = 'tracyrohlin'

from re import search

def parse_binary(bin_s):
    if not search("^[10]*$", bin_s):
        raise ValueError
    bin_s = [int(i) for i in bin_s]
    result = 0
    for i, e in zip(bin_s, enumerate(bin_s[::-1])):
        result += i * (2**e)
    return result

