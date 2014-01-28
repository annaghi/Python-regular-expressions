import re

def print_match(match):
    if match is None:
        print 'No match'
        return

    print "'{g}' was matched between the indices {s}".format(g=match.group(), s=match.span())
    return match


word = "infinity"


# Find the character 'i' at the beginning of the word
print re.findall(r"^i", word)
# ['i']


# Find all occurrences of the character 'i'
print re.findall(r"i", word)
# ['i', 'i', 'i']

# Find all non-overlapping two-character length substrings, where the second character is 'i'
print re.findall(r".i", word)
# ['fi', 'ni']


# Find all non-overlapping substrings ending with character 'i',
# where the preceding character exists or does not
print re.findall(r".?i", word)
# ['i', 'fi', 'ni']


# Find all non-overlapping substrings 'in'
print re.findall(r"i[n]", word)
# ['in', 'in']

# Find all non-overlapping substrings starting with character 'i',
# and ending with any character except 'n'
print re.findall(r"i[^n]", word)
# ['it']


# Perform a greedy searching for the substring starting and ending with the character 'i'
# (longest possible match)
print_match(re.search(r"i.*i", word))
# 'infini' was matched  between the indices (0, 6)

# Perform a non-greedy searching for the substring starting and ending with the character 'i'
# (shortest possible match)
print_match(re.search(r"i.*?i", word))
# 'infi' was matched  between the indices (0, 4)



single_line = "Looks like this sentence is not as simple as it looks"



#Perform a case-sensitive searching for the first occurrence of the word 'looks'
print_match(re.search(r"looks", single_line))
# 'looks' was matched  between the indices (48, 53)

# Perform a case-insensitive searching for the first occurrence of the word 'looks'
print_match(re.search(r"looks", single_line, re.IGNORECASE))
# 'looks' was matched  between the indices (0, 5)


# Perform a case-sensitive matching for the word 'looks'
print_match(re.match(r"looks", single_line))
# No match

# Perform a case-insensitive matching for the word 'looks'
print_match(re.match(r"looks", single_line, re.IGNORECASE))
# 'Looks' was matched  between the indices (0, 5)



# Orinoco Flow by Enya
multi_line = """Let me sail, let me sail
Let the Orinoco Flow
Let me reach, let me beach
On the shores of Tripoli"""



# Searching for the word 'sail' at the end of the string
print_match(re.search(r"sail$", multi_line))
# No match


# Searching for the word 'sail' at the end of any line
print_match(re.search(r"sail$", multi_line, re.MULTILINE))
# 'sail' was matched  between the indices (20, 24)


# Searching for the phrase 'beach On' with any character except newline between these two words
print_match(re.search(r"beach.On", multi_line))
# No match


#Searching for the phrase 'beach On' with any character between these two words
print_match(re.search(r"beach.On", multi_line, re.DOTALL))
# 'beach
# On' was matched  between the indices (67, 75)


# Searching for all the lines between the line containing the word 'reach',
# and the line ending with the word 'Tripoli'
print_match(re.search(r"^[^\n]*reach.*Tripoli$", multi_line, re.MULTILINE|re.DOTALL))
# 'Let me reach, let me beach
# On the shores of Tripoli' was matched  between the indices (46, 97)
