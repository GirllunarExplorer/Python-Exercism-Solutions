__author__ = 'tracyrohlin'

import collections

def handshake(n):
    secret_code = {1: "wink", 2: "double blink", 4: "close your eyes", 8: "jump"}
    secret_handshake = []
    rev = False
    if n <=0:
        return secret_handshake

    try:
        if isinstance(n, str):
            n = int("0b{}".format(n), 2)

        if n > 16:
            rev, n = True, (n-16)

        for key, value in sorted(secret_code.items()):
            if n & key == key:
                secret_handshake.append(value)

        if rev:
            secret_handshake.reverse()
        return secret_handshake

    except:
        return secret_handshake


def code(secret_list):
    number_code = 0
    numbers = collections.OrderedDict([("wink", 1), ("double blink", 2), ("close your eyes", 4), ("jump", 8)])
    keys = [bin(i) for i in numbers.keys()]

    for action in secret_list:
        if action not in keys: #checks to see if item is in dictionary
            return str(0)
        else:
            number_code += numbers[action]
    if all(numbers[f] < numbers[s] for f, s in zip(secret_list, secret_list[1:])) == False: #checks to see if items are out of order
        number_code += 10000

    return str(number_code)

