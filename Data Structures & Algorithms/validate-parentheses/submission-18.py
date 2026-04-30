class Solution:
    def isValid(self, s: str) -> bool:
        closeBrackets = {"}":"{", ")":"(", "]":"["}
        stack = []

        for b in s:
            if b in closeBrackets:
                if stack and stack[-1] == closeBrackets.get(b):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        return not stack
        

