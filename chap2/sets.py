from __future__ import division
from time import time

s = set()
s.add(1)
s.add(2)
s.add(2)
x = len(s)
print(2 in s)
print(3 in s)

from random_words import RandomWords
rw = RandomWords()
word = rw.random_word()
print(word)

word = rw.random_word('y')
print(word)

words = rw.random_words(count=10)
print(words)

words = rw.random_words(letter='r', count=5)
print(words)

words = rw.random_words(letter=None, count=2)
print(words)

hundreds_of_other_words = []

stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]
stopwords_list = rw.random_words(count=5000)
start = time()
print("zip" in stopwords_list)
stop = time()
print(stop - start)
stopwords_set = set(stopwords_list)
start = time()
print("zip" in stopwords_set)
stop = time()
print(stop - start)

item_list = [1, 2, 3, 1, 2, 3]
print(item_list)
num_items = len(item_list)
item_set = set(item_list)
num_distinct_items = len(item_set)
distinct_item_list = list(item_set)
print(distinct_item_list)

