# this is a sliding window problem, we can use a set to store the characters in the current window
## and use two pointers to move the window. The left pointer will move when we find a duplicate character.
# leetcode 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Sliding window technique is used to solve this problem.
# Time complexity: O(n)
# Space complexity: O(min(n, m)), where n is the length of the string and m is the size of the character set.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charset = set()
        res=0
        l=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res = max(res,r-l+1)

        return res
        
        