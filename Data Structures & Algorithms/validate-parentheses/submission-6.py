class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        closeBracketMap = {"]":"[","}":"{",")" : "("}


        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            elif stack and stack[-1] == closeBracketMap[c]:
                stack.pop()
            else: 
                return False
        return stack == []