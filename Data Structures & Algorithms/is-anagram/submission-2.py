class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}

        for i in s:
            if i in map1:
                map1[i] += 1
            else:
                map1[i] = 1
        
        for k in t:
            if k in map2:
                map2[k] += 1
            else:
                map2[k] = 1

        return True if (map1 == map2) else False
        