__author__ = 'tracyrohlin'

import string, random, re
from string import ascii_lowercase

class Cipher:
    def __init__(self, key=None):
        self.key = key or self.generate_key()
        self.asci_keys = dict((v,k) for (k,v) in enumerate(ascii_lowercase))
        self.num_keys = dict((k,v) for (k,v) in enumerate(ascii_lowercase))


    def generate_key(self):
        return ''.join(random.choice(string.ascii_lowercase) for n in range(100))

    def change(self, text, decode=False):
        new_sentence = re.sub("\d*\W+", "", text)
        text = list(new_sentence.lower())
        new_list =[]
        if len(self.key) < len(text):
            self.key += self.key[0]* (len(text)-len(self.key))

        for letter, key in zip(text, self.key):
            key_num, l = self.asci_keys[key], self.asci_keys[letter]
            let_num = key_num + l
            if decode:
                let_num = l - key_num
            new_list.append(self.num_keys[let_num% 26])

        return "".join(new_list)


    def encode(self, text):
        return self.change(text)

    def decode(self, text):
        return self.change(text, decode=True)


class Caesar(Cipher):
    def generate_key(self):
        return "d" * 100