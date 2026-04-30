class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        substring = set()
        maxLen = 0

        if len(s) == 1:
            return 1

        while r < len(s):
            if s[r] not in substring:
                substring.add(s[r])
                r += 1
                maxLen = max(maxLen, len(substring))
            else:
                substring.remove(s[l])
                l += 1
        return maxLen