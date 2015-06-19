__author__ = 'tracyrohlin'


lyrics = [["", ' the house that Jack built.\n\n'],
          ['that lay in', ' the malt\n'],
          ['that ate', ' the rat\n'],
          ['that killed', ' the cat\n'],
          ['that worried',' the dog\n'],
          ['that tossed', ' the cow with the crumpled horn\n'],
          ['that milked', ' the maiden all forlorn\n'],
          ['that kissed', ' the man all tattered and torn\n'],
          ['that married', ' the priest all shaven and shorn\n'],
          ['that woke', ' the rooster that crowed in the morn\n'],
          ['that kept', ' the farmer sowing his corn\n'],
          ["that belonged to", ' the horse and the hound and the horn\n']]
def recursive_noun_phrase(n):
    song = ""
    if n ==0:
        song += lyrics[0][1]
    else:
        first_verse, second_verse = lyrics[n]
        song += second_verse + first_verse + recursive_noun_phrase(n-1)

    return song

def rhyme():
    nursery_rhyme = ""
    for i in range(12):
        nursery_rhyme += "This is" + recursive_noun_phrase(i)
    return nursery_rhyme.strip()