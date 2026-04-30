class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = set(nums)
        for i in range(0, len(nums)):
            if target - nums[i] in numSet:
                num2 = target - nums[i]
                for j in range(0, len(nums)):
                    if nums[j] == num2 and j != i:
                        if i >= j:
                            return [j, i]
                        else:
                            return [i, j]
