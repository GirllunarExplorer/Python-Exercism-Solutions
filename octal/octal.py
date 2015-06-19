__author__ = 'tracyrohlin'


def parse_octal(num):
    acceptable = [str(i) for i in range(8)]
    result = 0
    e = len(num)-1
    for l in num:
        if l not in acceptable:
            raise ValueError("all octal numbers must be from 0 to 7")
        n = int(l)
        result += n* 8**e
        e-=1
    return result

parse_octal("1")