#
# Skeleton file for the Python "Bob" exercise.
#
import re
import string

def hey(what):
    what = what.strip()
    if re.search("^\s+$", what) or what == "":
        return 'Fine. Be that way!'
    elif what.isupper():
        return 'Whoa, chill out!'
    elif "?" == what[-1]:
        return "Sure."
    else:
       return 'Whatever.'

