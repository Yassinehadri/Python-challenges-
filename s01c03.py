with open("frankenstein.txt") as f:
    book = f.read()
    print(len(book))
from collections import Counter
from string import   ascii_letters,ascii_lowercase,ascii_uppercase
print(ascii_uppercase)
print(ascii_lowercase)
print(ascii_letters)
def get_freqs(text,letters):
   counts=Counter()
   for letter in letters :
    counts[letter]=text.count(letter)
   total=sum(counts.values())
   return {letter:counts[letter]/total for letter in letters}

#freqs_lower=get_freqs(book,ascii_lowercase)
#print("freqs of lower : ",freqs_lower)

freqs_letters=get_freqs(book,ascii_letters)
print("freqs of lower : ",freqs_letters)

#how to calculate frenquencies after that we should calculate error abs(actual_freq -expcted_freq)
......