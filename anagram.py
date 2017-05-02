 # -*- coding: utf-8 -*-
__author__ = 'ejm2095'

#The Anagram problem: Output the number of words w in a list of n words, such
# that at least one of the other n-1 words in the list is an anagram of w.
# A word is an anagram of itself. Ignore case. The input has only alpha characters. Example:
#anagram_count( ['Act', 'cat', 'cat', 'dog', 'dog', 'aardvark'] ) returns 5
def anagram_count(lst):
    count = 0
    chars = {}
    chars_relation = {}
    for word in lst:
        word = word.lower()
        letters = chars_relation.get(word)
        if not letters:
            c = list(word)
            c.sort()
            letters = "".join(c)
            chars_relation[word] = letters

        v = chars.get(letters,0)
        chars[letters]=v+1
        if v==1:
            count+=2
        elif v>1:
            count +=1
    return count

print anagram_count(['Act', 'cat', 'cat', 'dog', 'dog', 'aardvark'])
print anagram_count( ["touché", "étouch", "touche"] )