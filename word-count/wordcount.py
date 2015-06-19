__author__ = 'tracyrohlin'

from collections import defaultdict

def word_count(s):
    split_s = s.split()
    end_count = defaultdict(int)
    for item in split_s:
        end_count[item] +=1
    return end_count

