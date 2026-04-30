class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        best = 0
        letterMap = defaultdict(int)
        while r < len(s):
            letterMap[s[r]] += 1
            if ((r - l + 1) - max(letterMap.values())) > k:
                letterMap[s[l]] -= 1
                l += 1
            best = max(best, r-l+1)
            r += 1
        return best

#AAABABB
