class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1
        
        arr = []

        for num, cnt in seen.items():
            arr.append([cnt, num])
        
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])

        return res


        
        # 1 1
        # 2 3
        # 3 2

