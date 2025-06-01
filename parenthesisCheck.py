class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack:
                    return False
                top = stack.pop()
                if (top == '(' and char != ')') or \
                (top == '[' and char != ']') or \
                (top == '{' and char != '}'):
                    return False
        return len(stack) == 0