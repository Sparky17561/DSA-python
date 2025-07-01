#leetcode 


class Solution(object):
    def possibleStringCount(self, word):
        n = len(word)
        count = n
        for i in range(1, n):
            if word[i] != word[i - 1]:
                count -= 1
        return count
