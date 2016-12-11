import re


string = """<title>Babel</title>
<paragraph>
<sentence>Languages shape how you solve problems.</sentence>
<SENTENCE>Be curious learn a new language.</SENTENCE>
</paragraph>"""



############################################################################################
'(...)' # Matches whatever regular expression is inside the parentheses.
############################################################################################

it = tuple(re.finditer(r"<([\w]+)>", string))
    # return the entire match of each match
for match in it:
    print match.group()
# <title>
# <paragraph>
# <sentence>
# <SENTENCE>

# return the first parenthesized subgroup of each match
for match in it:
    print match.group(1)
# title
# paragraph
# sentence
# SENTENCE


############################################################################################
'(?aiLmsux)' # The letters set the corresponding flag for the entire regular expression.
############################################################################################

# Perform a case-sensitive searching for the pattern '<sentence>'.
it = re.finditer(r"<(sentence)>", string)
for match in it:
    print match.group(1)
# sentence


# Perform a case-insensitive searching for the pattern '<sentence>' using (?i) empty group.
it = re.finditer(r"<((?i)sentence)>", string)
for match in it:
    print match.group(1)
# sentence
# SENTENCE


############################################################################################
'match.group([1,..])' # Returns one or more subgroups of the match. 
############################################################################################

# Return three subgroups of each match.
it = tuple(re.finditer(r"<([\w]+)>(.*?)</([\w]+)>", string))

# Print the first subgroup of each match.
for match in it:
    print match.group(1)
# title
# sentence
# SENTENCE


# Print the first and the third subgroups of each match.
for match in it:
    print match.group(1,3)
# ('title', 'title')
# ('sentence', 'sentence')
# ('SENTENCE', 'SENTENCE')


############################################################################################
'(?:...)'        # A non-capturing version of regular parentheses.
'match.groups()' # Return a tuple containing all the subgroups of the match.
############################################################################################

# Return three subgroups of each match, and print all subgroups of each match.
it = re.finditer(r"(<[\w]+>)(.*?)(</[\w]+>)", string)
for match in it:
    print match.groups()
# ('<title>', 'Babel', '</title>')
# ('<sentence>', 'Languages shape how you solve problems.', '</sentence>')
# ('<SENTENCE>', 'Be curious learn a new language.', '</SENTENCE>')


# Return three subgroups of of each match, but non-captured versions cannot be retrieved.
it = re.finditer(r"(<[\w]+>)(?:.*?)(?:</[\w]+>)", string)
for match in it:
    print match.groups()
# ('<title>',)
# ('<sentence>',)
# ('<SENTENCE>',)



############################################################################################
'(?P<name>...)' # A named version of regular parentheses.
############################################################################################

# The substring matched by the group is accessible via the symbolic group name.
it = re.finditer(r"(<[\w]+>)(?P<text>.*?)(</[\w]+>)", string)
for match in it:
    print match.group('text')
# Babel
# Languages shape how you solve problems.
# Be curious learn a new language.


'(?P=name)' # A backreference to a named group.

# The backreference matches whatever text was matched by the earlier group named name.
it = re.finditer(r"<(?P<tag>[\w]+)>(?P<text>.+?)</(?P=tag)>", string)
for match in it:
    print match.group('text')
# Babel
# Languages shape how you solve problems.
# Be curious learn a new language.


