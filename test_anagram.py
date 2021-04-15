import anagram
import unittest

class TestAnagram(unittest.TestCase):
    def test_anagrams_(self):
        result = anagram.get_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
        assert.equals(result, ['aabb', 'bbaa'])

    def test_anagrams_return_words_different_len(self):
        result = anagram.get_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
        assert.equals(result, ['carer', 'racer'])

    def test_anagrams_return_two_empty_result(self):
        result = anagram.get_anagrams('laser', ['lazing', 'lazy', 'lacer'])
        assert.equals(result, [])
