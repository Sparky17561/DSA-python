# using zfill
# 1. Problem
# Given three integers, the task is to generate a key by taking the minimum digit from each corresponding position of the three integers.
# 2. Solution
# The solution involves converting each integer to a string, padding it with leading zeros to ensure they are all 4 digits long, and then comparing the digits at each position.
# 3. Implementation

class Solution(object):
    def generateKey(self, num1, num2, num3):
        """
        :type num1: int
        :type num2: int
        :type num3: int
        :rtype: int
        """
        s1 = str(num1).zfill(4)
        s2 = str(num2).zfill(4)
        s3 = str(num3).zfill(4)

        key = ""
        for i in range(4):
            key += min(s1[i], s2[i], s3[i])
        return int(key)

        

# my approach brute force 


class Solution(object):
    def generateKey(self, num1, num2, num3):
        """
        :type num1: int
        :type num2: int
        :type num3: int
        :rtype: int
        """
        num1 = str(num1)
        num2 = str(num2)
        num3 = str(num3)

        key =''

        if len(num1) < 4:
            n = 4 - len(num1)
            num1 = '0'*n + num1

        if len(num2) < 4:
            n = 4 - len(num2)
            num2 = '0'*n + num2

        if len(num3) < 4:
            n = 4 - len(num3)
            num3 = '0'*n + num3


        i = 0

        while i < 4:
            key += min(num1[i],num2[i],num3[i])
            i+=1
        
        return int(key)