__author__ = 'tracyrohlin'


def check_palindrome(max_factor=None, min_factor=0):
    palindrome_list = []
    for x in yield_product(max_factor, min_factor):
        if str(x[0])[:] == str(x[0])[::-1]:
            palindrome_list.append(x)
    return palindrome_list

def largest_palindrome(max_factor=None, min_factor=0):
    palindrome = max(check_palindrome(max_factor, min_factor))
    return palindrome[0], {palindrome[1], palindrome[2]}

def smallest_palindrome(max_factor=None, min_factor=0):
    palindrome = min(check_palindrome(max_factor, min_factor))
    return palindrome[0], {palindrome[1], palindrome[2]}

def yield_product(max_factor, min_factor):
    for n in range(min_factor, max_factor+1):
        for x in range(min_factor, max_factor+1):
            yield [x*n, x, n]

