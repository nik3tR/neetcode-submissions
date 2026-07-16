class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHashMap = defaultdict(int)
        tHashMap = defaultdict(int)
        if len(s) != len(t) or not (s or t):
            return False
        
        for i in range(0, max(len(s), len(t))):
            sHashMap[s[i]] += 1
            tHashMap[t[i]] += 1
        
        return sHashMap == tHashMap


        