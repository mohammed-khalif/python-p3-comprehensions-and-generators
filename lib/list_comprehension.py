#!/usr/bin/env python3

def return_evens(num_list):
    pass

def make_exclamation(sentence_list):
    pass
# lib/list_comprehension.py

def return_evens(sequence):
    return [num for num in sequence if num % 2 == 0]

def make_exclamation(sentences):
    return [sentence + '!' for sentence in sentences]

# tests/test_list_comprehension.py

from lib.list_comprehension import return_evens, make_exclamation

def test_return_evens():
    assert return_evens([0, 1, 3, 5, 7, 8, 9]) == [0, 8]
    assert return_evens([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]
    assert return_evens([1, 3, 5, 7, 9]) == []
    assert return_evens([]) == []

def test_make_exclamation():
    assert make_exclamation(["Hello", "I'm doing great", "Python is fun"]) == ["Hello!", "I'm doing great!", "Python is fun!"]
    assert make_exclamation(["Testing", "One", "Two", "Three"]) == ["Testing!", "One!", "Two!", "Three!"]
    assert make_exclamation([]) == []

