"""
pseudocode:
set text
change text to text_list
print text_list

set word_count = {}
for word in text_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word in sorted(word_count):
    print(f"{word}:{word_count[word]")

"""

text = "this is a collection of words of nice words this is a fun thing it is"
text_list = text.split()
print (text_list)

word_count = {}
for word in text_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word in sorted(word_count):
    print(f"{word} : {word_count[word]}")




"""
Word Occurrences
Estimate: 10 minutes
Actual:   8 minutes
"""