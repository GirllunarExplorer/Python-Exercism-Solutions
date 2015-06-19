__author__ = 'tracyrohlin'

from difflib import SequenceMatcher
song1 = "this_is_a_song.mp3"

song2 = "this is a song remix.mp3"

seq = SequenceMatcher(None, song1,song2)

print seq.ratio()
