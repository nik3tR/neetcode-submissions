class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0

        maxL = 0
        seen = set()
        currMax = 0
        while r < len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                r += 1
                maxL = max(maxL, r - l)
        return maxL