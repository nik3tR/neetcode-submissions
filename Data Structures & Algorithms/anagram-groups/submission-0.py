class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        for string in strs:
            sortString = ''.join(sorted(string))
            if sortString in myMap:
                myMap[sortString].append(string)
            else: myMap[sortString] = [string]
        return myMap.values()


