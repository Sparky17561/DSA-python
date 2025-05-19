# brute force
# Time complexity: O(n)

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        from collections import Counter

        n = len(words)
        count_c = Counter()

        for word in words:
            count_c.update(word)

        for freq in count_c.values():
            if freq % n != 0:
                return False

        return True





# optimal solution
# Time complexity: O(n)

class Solution(object):
    def makeEqual(self, words):
        s = "".join(words)          # Step 1: Concatenate all words into one string
        t = set(s)                  # Step 2: Get all unique characters
        l = len(words)              # Step 3: Number of words
        
        for i in t:                 # Step 4: For each unique character
            if s.count(i) % l != 0:  # If the total count is not divisible by number of words
                return False         # Cannot split it evenly → return False
        
        return True  # All characters can be evenly divided → return True
