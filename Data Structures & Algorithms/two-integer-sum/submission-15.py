class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(0, len(nums)):
            numMap[nums[i]] = i
        
        for j in range(0, len(nums)):
            diff = target - nums[j]
            if diff in numMap and numMap[diff] != j:
                return [j, numMap[diff]]
