import re

def print_match(match):
    if match is None:
        print 'No match'
        return

    print match.group()
    return match



string = "begin:id1:tag:id2:tag:id3:end"


'(?=...)' # Positive lookahead assertion
# Matches if '...' matches next.
print re.findall(r"(id\d+)(?=:tag)", string)
# ['id1', 'id2']


'(?!...)' # Negative lookahead assertion
# Matches if '...' does not match next.
print re.findall(r"(id\d+)(?!:tag)", string)
# ['id3']


'(?<=...)' # Positive lookbehind assertion
# Matches if the searched substring is preceded by a match for '...'.
# Note that the contained pattern must only match strings of some fixed length.
print re.findall(r"(?<=id\d:)(\b\w*\b)", string)
# ['tag', 'tag', 'end']


'(?<!...)' # Negative lookbehind assertion
# Matches if the searched substring is not preceded by a match for '...'.
# Note that the contained pattern must only match strings of some fixed length.
print re.findall(r"^(?<!:tag)(\b\w*\b)", string)
# ['begin']


'(?(id/name)yes-pattern|no-pattern)'
# Will try to match with yes-pattern if the group with given id or name exists,
# and with (optional) no-pattern if it does not.
print_match(re.match("(<)?[^<]*(?(1)>)", "<identifier>text"))
# <identifier>

print_match(re.match("(<)?[^<]*(?(1)>)", "text<identifier>"))
# text
