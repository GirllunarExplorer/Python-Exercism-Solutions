__author__ = 'tracyrohlin'


def trinary(num):
    acceptable = [str(i) for i in range(3)]
    result = 0
    e = len(num)-1
    for l in num:
        if l not in acceptable:
            return 0
        n = int(l)
        result += n* 3**e
        e-=1
    return result

print trinary('13201')