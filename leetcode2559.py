# 2559. Count Vowel Strings in Ranges
# https://leetcode.com/problems/count-vowel-strings-in-ranges/
class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(words)
        prefix_sum = [0] * (n+1)

        for i,c in enumerate(words):
            if c[0] in "aeiou" and c[-1] in "aeiou" :
                prefix_sum[i+1] += prefix_sum[i] +1
            else:
                prefix_sum[i+1] = prefix_sum[i]
                
                    

        result = []
        for l, r in queries:
            count = prefix_sum[r+1] - prefix_sum[l]
            result.append(count)
        return result