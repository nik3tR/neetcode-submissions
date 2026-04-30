class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index1, index2 = 0, 0
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in nums:
                index1 = i
                for j in range(len(nums)):
                    if nums[j] == num2 and j != index1:
                        index2 = j
                        break
        return sorted([index1,index2])