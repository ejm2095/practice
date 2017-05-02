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
import operator
import functools

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

def placementWRONG(word):
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

def placement(word):
    word_base = word

    sorted_word_uniques = list(set(word))
    sorted_word_uniques.sort()
    place = 0
    index = 0
    for letter in word_base:
        if len(word_base[index+1:]):
            letters_before = sorted_word_uniques.index(letter)
            added_place= (letters_before*possibilities(word_base[index+1:]) | 1)
            print 'letters_before: {} possibilities:{} word_base[index+1:]: {} added_place: {}'.format(letters_before, possibilities(word_base[index+1:]), word_base[index+1:], added_place)
            place += added_place
            index += 1
            sorted_word = get_sorted_word(word_base[index:])
            sorted_word_uniques = list(set(sorted_word))
            sorted_word_uniques.sort()
    return place

def get_sorted_word(word):
    list_word = list(word)
    list_word.sort()
    return list_word

def possibilities(word):
    total_letters = len(word)
    repeated_letter = {}
    for letter in word:
        repeated_letter[letter] = repeated_letter.get(letter, 0) + 1
    return factorial(total_letters)/ functools.reduce(operator.mul, [factorial(x) for x in repeated_letter.values()], 1)


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
        print placement(choice)
