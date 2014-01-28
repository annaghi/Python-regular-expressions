import re
from pprint import pprint


lines = """BLOCK BEGIN 01
Text in the first block.
BLOCK END 01
BLOCK BEGIN 02
More text in the second block.
And some more text in the second block.
BLOCK END 02
BLOCK BEGIN 03
Text in the third block.
BLOCK END 03
"""
lines = lines.splitlines()

# dictionary for collecting blocks of the file
blocks = {}


# begin block transitional event
begin = re.compile(r"^BLOCK BEGIN (?P<key>[\d]{2})$")

# end block transitional event
end = re.compile(r"^BLOCK END [\d]{2}$")

# new block state
new_block = False

# initialize globals
block = key = ''


for line in lines:

    if new_block:

        if end.match(line):
            blocks[key] = block
            new_block = False
            block = key = ''

        else :
            block += line + '\n'

    else:
        if begin.match(line):
            match = re.match(begin, line)
            key = match.group('key')
            new_block = True


pprint(blocks)
