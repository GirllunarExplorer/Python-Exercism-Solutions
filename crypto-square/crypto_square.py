__author__ = 'tracyrohlin'

import re, math

def encode(passage):
    if passage:
        passage = (re.sub("\W+","", passage)).lower()
        num_of_rows = int(math.floor((len(passage)) ** 0.5))
        num_of_col = int(math.ceil(float(len(passage))/ num_of_rows))

        chunked_passage = []
        start = 0
        end = num_of_col
        while len(chunked_passage) < num_of_rows: #creates square/rectangle of chunked words
            chunked_passage.append(passage[start:end])
            start = end
            end += num_of_rows+1
        print chunked_passage


        ciph_list = []
        for i in range(len(chunked_passage[0])):  #checks the length of the first chunk, which is the longest
            subword = []
            for chunk in chunked_passage: #goes through each word and picks the ith element and appends to subword
                if i < len(chunk):
                    subword.append(chunk[i])
            ciph_list.append("".join(subword))

        return " ".join(ciph_list)

    return passage
msg = "1, 2, 3, Go! Go, for God's sake!"
print encode(msg)