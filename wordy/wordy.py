__author__ = 'tracyrohlin'

import operator
from scipy import where, array

def calculate(mathstring):
    if not mathstring.endswith("?") or not mathstring.startswith("What is"):
        raise ValueError("This is not a valid question")


    ops = {"plus": operator.add,
           "minus": operator.sub,
           "multiplied": operator.mul,
           "times": operator.mul,
           "divided": operator.div,
           "raised": operator.pow}
    elements = mathstring.split()[2:]
    elements[-1] = "".join(list(elements[-1])[:-1])

    elements = [w for w in elements if w != "by"]

    if "raised" in mathstring:
        loc = where(array(elements) == "raised") #finds all raised powers in order to join the string for later dict search
        for j in loc:
            j = int(j)
            elements[j] = " ".join(elements[j:j+1])
            elements[j+3] = elements[j+3][:-2]  #removes the "nth" from the string
        for word in ["to", "the", "power"]:
            elements.remove(word)

    result = int(elements[0])
    for i in range(1, len(elements), 2):
        try:
            oper = ops[elements[i]]
            result = oper(result, int(elements[i+1]))
        except: raise ValueError("That operation does not exist in the dictionary")
    return result

