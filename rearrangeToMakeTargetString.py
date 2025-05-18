# similar to Balloon problem

from collections import Counter
class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """

        word = Counter(s)
        t = Counter(target)
        res = len(s)

        for i in t:
            res = min(res,word[i]//t[i])

        return res

        