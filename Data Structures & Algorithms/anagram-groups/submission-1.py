class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        AnagramMap = {}

        for i in strs:
            stringSorted = "".join(sorted(i))
            if stringSorted in AnagramMap:
                AnagramMap[stringSorted].append(i)
            else: 
                AnagramMap[stringSorted] = [i]

        return AnagramMap.values()