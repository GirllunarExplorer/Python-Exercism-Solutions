__author__ = 'tracyrohlin'

class DNA(object):
    def __init__(self, stringA):
        super(DNA, self).__init__()
        self.stringA = stringA


    def hamming_distance(self, stringB):
        result = 0
        for i, j in zip(list(self.stringA), list(stringB)):
            if i !=j:
                result +=1
        return result