"""
Solution to AthenaHealth's coding problem

The solution looks at the number of possible outcomes as a tree
similar to how game theory looks at the possible moves in a finite "game"
using this strategy it can be determined how many words can be made using
this number of letters.  Once that is know, it's time to be a lumberjack and trim
the "tree" down look at how the minimum number of possible outcomes that would
occur before.
"""

from math import factorial, ceil
import itertools

#step one find a solution that fits words with no repeat letters
#works for words such as QUESTION and CABD
def placement_no_repeats(word):
    n = len(word) #get the length of the word
    branches = factorial(n) #find the number of possibilities
    # First convert the word to a list
    # Next sort the list, this is how to determine how many words are "in front"
    lst_word = list(word)
    lst_word.sort()
    #set the rank to the best possible outcome
    rank = 1
    #Following a binary search algorithm find and count the number of possible "branches"
    # or outcomes come before this word.
    for i in xrange(0,n):
        node = lst_word.index(word[i])
        branches /=(n-i)
        rank += branches * node
        lst_word.remove(word[i])

    print "%s %d" % (word, rank)

def placement(word):
    n = len(word) #get the length of the word
    branches = factorial(n)/repeats(word) #find the number of possibilities
    # First convert the word to a list
    # Next sort the list, this is how to determine how many words are "in front"
    lst_word = list(word)
    lst_word.sort()
    d_chars = {}
    d_spent = {}
    for i in set(lst_word):
        d_chars[i] = lst_word.count(i)
        d_spent[i] = 1
    #set the rank to the best possible outcome
    rank = 1
    #Following a binary search algorithm find and count the number of possible "branches"
    # or outcomes come before this word.
    d_l_char = d_chars.keys()
    d_l_char.sort()
    for i in xrange(0,n):
        node = lst_word.index(word[i])
        branches = (ceil(float(branches)/float(n-i)))*d_spent.get(word[i])
        v=0
        d_l_char.sort()
        for x in range(0,d_l_char.index(word[i])):
            v += branches*d_chars[d_l_char[x]]
        rank += v
        lst_word.remove(word[i])
        d_chars[word[i]] -=1
        if not d_chars[word[i]]:
            d_l_char.remove(word[i])
        d_spent[word[i]]+=1

    print "%s %d" % (word, rank)

#simple function to count the number of repeats
def repeats(word):
    awn = 1
    i =0
    d = {}
    while i < len(word):
        x = word[i]
        p = d.get(x)
        if not p:
            d[x] = 1
        if p:
            d[x] +=1
        i += 1
    for i in d.values():
        awn *= factorial(i)
    return awn


choice = ""
print """Consider a word as ANY sequence of at least 2 capital letters A-Z.  We can then assign a number to every word,
based on where it falls in an alphabetically sorted list of all words made up of the same set of letters."""
while choice != "-1":
    print
    choice = raw_input("Enter a word to test or -1 to exit: ")
    if choice != "-1":
        placement(choice)
