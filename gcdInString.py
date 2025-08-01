# leetCode 1071. Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a

        if str1 + str2 != str2 + str1:
            return ""
        else:
            gcd_len = gcd(len(str1),len(str2))
            return str1[:gcd_len]        