class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        n = len(num)
        counter=0
        number=0
        maxi=-1

        for i in range(n-2):
            if num[i] == num[i+1] == num[i+2]:
                d=int(num[i])
                if d > maxi:
                    maxi=d

        if maxi < 0:
            return ""
        
        return str(maxi)*3