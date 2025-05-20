class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
    
        result = []
        for char in set(words[0]):
            min_count = min(word.count(char) for word in words)
            result += [char] * min_count
        return result