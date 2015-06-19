__author__ = 'tracyrohlin'

import string, random, re
from string import ascii_lowercase

class Cipher:
    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            self.key = self.generate_key()
        self.asci_keys = dict((v,k) for (k,v) in enumerate(ascii_lowercase))
        self.num_keys = dict((k,v) for (k,v) in enumerate(ascii_lowercase))


    def generate_key(self):
        return ''.join(random.choice(string.ascii_lowercase) for n in range(100))



    def encode(self, text):
        new_sentence = re.sub("\d*\W+", "", text)
        text = list(new_sentence.lower())
        self.key = self.key[:len(text)]
        new_list = []
        for letter, key in zip(text, self.key):
            key_num, l = self.asci_keys[key], self.asci_keys[letter]
            try:
                new_list.append(self.num_keys[key_num+l])
            except:
                new_list.append(self.num_keys[key_num+l-26])


        return "".join(new_list)

    def decode(self, text):
        new_sentence = re.sub("\d*\W+", "", text)
        text = list(new_sentence.lower())
        self.key = self.key[:len(text)]
        new_list = []
        print self.key
        for letter, key in zip(text, self.key):
            key_num, l = self.asci_keys[key], self.asci_keys[letter]
            try:
                new_list.append(self.num_keys[l-key_num])
            except:
                new_list.append(self.num_keys[l-key_num+26])


        return "".join(new_list)


class Caesar(Cipher):
    def generate_key(self):
        return "d" * 100