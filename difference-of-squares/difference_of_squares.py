__author__ = 'tracyrohlin'

def square_of_sum(n):
    n_list = list(range(1,n+1))
    square_sum = sum(n_list) ** 2
    return square_sum

def sum_of_squares(n):
    n_list = list(range(1,n+1))
    sum_num = sum(map(lambda n: n**2, n_list))

    return sum_num

def difference(n):
    return square_of_sum(n) - sum_of_squares(n)
