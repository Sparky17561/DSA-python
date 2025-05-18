class Solution:
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_set = set(allowed)
        res = len(words)
        for word in words:
            for char in word:
                if char not in allowed_set:
                    res -= 1
                    break
        return res
    


# using Bitmask
