class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        count =0

        for i in range(len(s)):
            if i%2: # odd should show 1
                if s[i] == '0':
                    count+=1
            else:
                if s[i] == '1':
                    count+=1

        return min(count,len(s)-count)
