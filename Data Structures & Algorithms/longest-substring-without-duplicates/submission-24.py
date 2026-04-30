class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0

        maxL = 0
        seen = set()
        currMax = 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                maxL = max(maxL, r - l)
            else:
                seen.remove(s[l])
                l += 1
        return maxL



# s="dvdf"
# d r = 1
# dv r = 2
# dvd (0, 2-0 = 2) maxL = 2
# "vd" r = 3

# abcc 
# a b c c
# a
# a b 
# a b c
# a b c c !!
# b c c !!
# c c !!



# 1 2 3 4 5
# 1
# (1, )