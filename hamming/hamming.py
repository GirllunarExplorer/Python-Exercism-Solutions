__author__ = 'tracyrohlin'

def distance(string_1, string_2):
    result = 0
    for i, j in zip(list(string_1), list(string_2)):
        if i !=j:
            result +=1
    return result

print distance('GATACA', 'GCATAA')