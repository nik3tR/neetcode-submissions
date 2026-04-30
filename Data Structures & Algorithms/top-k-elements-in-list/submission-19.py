class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for num in nums: # {2: 5, 3: 4, 1: 2}
            res[num] = 1 + res.get(num, 0)
        
        arr = []

        for num, cnt  in res.items():
            arr.append([cnt,num])
        arr.sort()
        print(arr)

        output = []
        while len(output) < k:
            output.append(arr.pop()[1])
        
        return output