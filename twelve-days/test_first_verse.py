__author__ = 'tracyrohlin'

def days_of_christmas(n):
    n-=1
    numbers = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth",
               "ninth", "tenth", "eleventh", "twelfth"]
    lyric = 'On the {0} day of Christmas my true love gave to me,'.format(numbers[n])
    return lyric


print days_of_christmas(8)