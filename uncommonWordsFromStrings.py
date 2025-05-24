from collections import Counter

# Given two sentences s1 and s2, return a list of all the uncommon words.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# we can use a.symmetric_difference() to find the uncommon words.but it fails to return the words that are not present in both sentences.

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        res=[]
        total = s1 + " " + s2
        count = Counter(total.split(" "))

        for c in count:
            if count[c] == 1:
                res.append(c)

        return res