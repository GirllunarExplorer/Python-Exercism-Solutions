__author__ = 'tracyrohlin'


def score(word):
    scrabble_values = {1: ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"],
                       2: ["d", "g"],
                       3: ["b", "c", "m", "p"],
                       4: ["f", "h", "v", "w", "y"],
                       5: ["k"],
                       8: ["j", "x"],
                       10: ["q", "z"]}
    if word:
        word = word.lower()
        new_scrabble_score = sum([k for (k,v) in scrabble_values.items() for l in list(word) if l in v])
        return new_scrabble_score
    else:
        return 0


