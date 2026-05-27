class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {"(": ")", "{": "}", "[": "]"}
        n = len(s)

        if n % 2 != 0:
            return False
        
        for char in s:
            if char in pairs:
                stack.append(char)
            else: 
                if not stack:
                    return False
                top = stack[-1]
                if pairs[top] == char:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0