__author__ = 'tracyrohlin'

def christmas_gifts(n):
    gifts = {1: " and a Partridge in a Pear Tree.\n", 2: " two Turtle Doves,", 3: " three French Hens,",
               4: " four Calling Birds,", 5: " five Gold Rings,", 6: " six Geese-a-Laying,",
               7: ' seven Swans-a-Swimming,', 8: " eight Maids-a-Milking,",
                9: " nine Ladies Dancing,", 10: ' ten Lords-a-Leaping,',
                11: ' eleven Pipers Piping,', 12: " twelve Drummers Drumming,"}
    new_verse = gifts[n]

    if n == 1:
        lyric = new_verse
    else:
        lyric = new_verse + christmas_gifts(n-1)


    return lyric

