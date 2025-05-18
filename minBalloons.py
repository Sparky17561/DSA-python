class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        #keep track of the number of each of the chars
        map_char = {}
        for char in "balloon":
            map_char[char] = 0
        
        
        for char in text:
            if char in "balloon":
                map_char[char]+=1

        map_char['l'] //= 2
        map_char['o'] //= 2
        return min(map_char.values())
        

# using counter

from collections import Counter

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = Counter(text)
        word = Counter("balloon")
        res = len(text)

        for i in word:
            res = min(res,count[i]//word[i])

        return res
        
                