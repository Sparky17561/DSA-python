class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        words = sentence.split()
        

        for i in range(1,len(words)):
            if words[i-1][-1] != words[i][0]:
                return False

        return words[-1][-1] == words[0][0]