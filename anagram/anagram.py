__author__ = 'tracyrohlin'

def detect_anagrams(word, str_a):
    word = word.lower()
    split_word = sorted(list(word))
    list_of_anagrams = []

    for item in str_a:
        lower_item = item.lower()
        if len(word) == len(lower_item) and lower_item != word:
            split_item = list(lower_item)
            split_item.sort()
            if split_item == split_word:
                list_of_anagrams.append(item)

    return list_of_anagrams


