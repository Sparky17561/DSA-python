# brute force
# Time complexity: O(n^2)
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxi=-1
        count=0
        n = len(s)
        for i in range(n):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    count = j-i-1
                    maxi = max(maxi,count)

        return maxi
        
#
# Optimized
# Time complexity: O(n)

class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxi=-1
        char_at = {} # to record their first occurence

        for i,c in enumerate(s):
            if c in char_at:
                maxi = max(maxi,i-char_at[c]-1)
            else:
                char_at[c] = i


        return maxi
        