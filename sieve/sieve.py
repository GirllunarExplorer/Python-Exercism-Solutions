__author__ = 'tracyrohlin'

def sieve(n):

    number_list = range(2, n+1)
    for i in range(n):
        for item in number_list[i+1:]: #checking the section of the list from the next number up
            if item % number_list[i] == 0:
                number_list.remove(item) #if any number further in the list is a multiple of the current number,
                                        # it removes ("filters") the number
    return number_list
print sieve(2)