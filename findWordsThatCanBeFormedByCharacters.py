

from collections import Counter,defaultdict


class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        count = Counter(chars)

        res = 0

        for w in words:
            curr_word = defaultdict(int)
            good=True
            for c in w:
                curr_word[c] += 1
                if c not in chars or curr_word[c] > count[c]:
                    good=False
                    break

            if good:
                res += len(w)
        return res
            
