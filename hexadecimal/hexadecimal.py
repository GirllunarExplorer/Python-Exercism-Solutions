__author__ = 'tracyrohlin'


def hexa(n):
    hex_dict = dict(zip("0123456789ABCDEF", range(16)))
    result = 0
    for exponent, integer in enumerate(n[::-1]):
        result += hex_dict[integer.upper()]* 16**exponent

    return result