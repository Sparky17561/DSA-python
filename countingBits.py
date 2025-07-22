# leetcode 338. Counting Bits
# https://leetcode.com/problems/counting-bits/


class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        for i in range(n+1):
            bin_no = bin(i)
            #bin_no = format(i,'b') #another way
            ones_count = bin_no.count('1')
            res.append(ones_count)

        return res