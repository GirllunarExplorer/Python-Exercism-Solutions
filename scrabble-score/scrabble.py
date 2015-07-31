__author__ = 'tracyrohlin'


def score(word):
    scrabble_values = {
        "a": 1, "n": 1,
        "b": 3, "o": 1,
        "c": 3, "p": 3,
        "d": 2, "q": 10,
        "e": 1, "r": 1,
        "f": 4, "s": 1,
        "g": 2, "t": 1,
        "h": 4, "u": 1,
        "i": 1, "v": 4,
        "j": 8, "w": 4,
        "k": 5, "x": 8,
        "l": 1, "y": 4,
        "m": 3, "z": 10,
    }


    word = word.lower()
    score = sum(scrabble_values.get(l, 0) for l in word)
    return score