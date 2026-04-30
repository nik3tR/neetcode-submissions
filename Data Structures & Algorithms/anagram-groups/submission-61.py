class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = defaultdict(list)

        for word in strs:
            s_word = sorted(word)
            seen[tuple(s_word)].append(word)
        
        res = []
        for n in seen.values():
            res.append(n)

        return res