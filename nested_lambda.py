"""
Let us assume that we have a text with list of names in it.
The aim is to replace the list of names with list of phone numbers.
"""

import re

# dictionary with name - phone number items
phone_book = {
  'Armin':    '11111',
  'Benedict': '22222',
  'Ceila':    '33333',
  'Dorina':   '44444' }


string = """Armin's friends are [Benedict, Dorina], and his phnoe number is \[11111\].
Benedict has a girlfiernd [Ceila].
Ceila is stranger to [Armin], and her phone number is \[33333\].
Dorina knows [Armin, Benedict, Ceila]."""



phone_numbers = r'(?P<name>%s)' % r'|'.join( phone_book.keys())

# Usage of the re.sub(pattern, function, string)

print re.sub(
    # pattern: grouping the [...] pattern into three named groups,
    # one for left square bracket, one for the names, and one for the right square bracket
    r"(?P<left>(?<!\\)\[)(?P<names>.*?)(?P<right>(?<!\\)\])",

    # replacement is produced by concatenation of three substrings
    lambda m1:
        # (1) replace [ with \[
        re.sub( r"\[", r"\[", m1.group('left')
        +
        # (2) Perform a nested re.sub() function on the named group 'list',
        # replacing the names with the phone numbers.
        re.sub(
            # pattern
            phone_numbers,
            # replace the name with the corresponding phone-number
            lambda m2: '{number}'.format(number=phone_book[m2.group('name')]),
            # string
            m1.group('names'))
        +
        # (3) replace ] with \]
        re.sub( r"\]", r"\]", m1.group('right'))
        ),

    # string
    string
)
# Armin's friends are \[22222, 44444\], and his phnoe number is \[11111\].
# Benedict has a girlfiernd \[33333\].
# Ceila is stranger to \[11111\], and her phone number is \[33333\].
# Dorina knows \[11111, 22222, 33333\].
