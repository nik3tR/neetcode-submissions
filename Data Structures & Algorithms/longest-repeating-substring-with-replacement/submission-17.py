class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        print(chars)
        maxLength = 0
        l, r = 0, 0

        for char in chars:
            print(char)
            l, r = 0, 0
            replacements = 0
            while r < len(s):
                print(l, r, s[r], replacements, maxLength)
                if s[r] != char:
                    replacements += 1
                if replacements > k:
                    if s[l] != char:
                        replacements -= 1
                    l += 1
                maxLength = max(maxLength, r - l + 1)
                r += 1
        
        return maxLength