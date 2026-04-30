class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        substring = s[l:r] #a
        maxLen = 0

        if len(s) == 1:
            return 1

        while r < len(s):
            if s[r] not in substring:
                r += 1
                substring = s[l:r]
                maxLen = max(maxLen, len(substring))
            else:
                l += 1
                substring = s[l:r]
        return maxLen