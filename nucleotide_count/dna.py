__author__ = 'tracyrohlin'

import re

class DNA(object):
    def __init__(self, string):
        super(DNA, self).__init__()
        self.string = string
        self.nucleotides = ["G", "A", "C", "T", "U"]

    def count(self, letter):
        if letter not in self.nucleotides:
            raise ValueError("{} is not a nucleotide".format(letter))
        if not self.string:
            return 0

        count = len(re.findall(letter, self.string))
        return count

    def nucleotide_counts(self):
        nucleo_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for letter in self.string:
            nucleo_counts[letter]+=1
        return nucleo_counts

print DNA("").nucleotide_counts()