import re


string = "Once you have accomplished small things, you may attempt great ones safely."

# Return all words beginning with letter 'a', as a list of strings
print re.findall(r"\ba[\w]+", string)
# ['accomplished', 'attempt']


# Return all words beginning with letter 'a', as an iterator yielding match objects
it = re.finditer(r"\ba[\w]+", string)
for match in it:
    print "'{g}' was found between the indices {s}".format(g=match.group(), s=match.span())
# 'accomplished' was found between the indices (14, 26)
# 'attempt' was found between the indices (49, 56)



# Split string by any character which is not a UNICODE word character
print re.split("\W+", string)
# ['Once', 'you', 'have', 'accomplished', 'small', 'things', 'you', 'may', 'attempt', 'great', 'ones', 'safely', '']

# Split string by any character which is not a UNICODE word character at most 2 split
print re.split("\W+", string, 2)
# ['Once', 'you', 'have accomplished small things, you may attempt great ones safely.']

# If the splitting pattern does not occur in the string, string is returned as the first element of the list
print re.split("(:)", string)
# ['Once you have accomplished small things, you may attempt great ones safely.']



# Replace all occurrences of space, comma, or dot with colon
print re.sub("[ ,.]", ":", string)
# Once:you:have:accomplished:small:things::you:may:attempt:great:ones:safely:

# Replace maximum 2 occurences of pattern
print re.sub("[ ,.]", ":", string, 2)
# Once:you:have accomplished small things, you may attempt great ones safely.

# Replace as 'sub', and return a tuple of (new string, number of replacements)
print re.subn("[ ,.]", ":", string)
# ('Once:you:have:accomplished:small:things::you:may:attempt:great:ones:safely:', 13)



# Find all five characthers long words
print re.findall(r"\b\w{5}\b", string)
# ['small', 'great']

# Find all five, six, or seven characthers long words
print re.findall(r"\b\w{5,7}\b", string)
# ['small', 'things', 'attempt', 'great', 'safely']

# Find all words which are at least 8 characters long
print re.findall(r"\b\w{8,}\b", string)
# ['accomplished']
