__author__ = 'tracyrohlin'


from test_recur import christmas_gifts
from test_first_verse import days_of_christmas

def verse(n):
    lyric = days_of_christmas(n) + christmas_gifts(n)
    if n == 1:
        mystring = lyric.replace(" and", "")
        return mystring
    return lyric

def verses(b, e):
    lyrics = ""
    for n in range(b,e+1):
        if verse(n)[-1] == "\n":
            lyric = verse(n) + "\n"
            lyrics += lyric
        else:
            lyric = verse(n) + "\n\n"
            lyrics += lyric

    return lyrics

def sing():
    return verses(1, 12)
