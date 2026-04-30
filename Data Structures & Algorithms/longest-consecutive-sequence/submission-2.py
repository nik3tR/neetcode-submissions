class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSub = []
        for num in nums:
            if num-1 not in numSet:
                tempSub = []
                tempSub.append(num)
                while num+1 in numSet:
                    tempSub.append(num+1)
                    num += 1
                if len(tempSub) > len(longestSub):
                    longestSub = tempSub
        return len(longestSub)

