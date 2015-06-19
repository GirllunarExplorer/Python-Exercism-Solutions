__author__ = 'tracyrohlin'

def keep(list, function):
    result = filter(function,list)
    return result

def discard(a_list, function):
    g = function
    temp = filter(function, a_list)
    result = [x for x in a_list if x not in temp]
    return result

inp = [2, 4, 6, 8, 10]

print discard(inp, lambda x: x % 2 == 0)