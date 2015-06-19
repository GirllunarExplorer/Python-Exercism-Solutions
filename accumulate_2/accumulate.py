__author__ = 'tracyrohlin'

def accumulate(nums, function):
    if not nums:
        return []
    result = [function(n) for n in nums]

    print result

inp = [10, 17, 23]

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print sum(foo)