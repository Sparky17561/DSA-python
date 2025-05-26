# Given a string s, sort it in decreasing order based on the frequency of characters.
# The frequency of a character is the number of times it appears in the string.
# leetcode 451


from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)  # Count frequency of each character
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return ''.join([char * times for char, times in sorted_chars])
