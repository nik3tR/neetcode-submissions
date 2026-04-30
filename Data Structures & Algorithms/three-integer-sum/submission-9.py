class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums) - 2:
            if nums[i] > 0:
                break
            l, r = i+1, len(nums) - 1
            while l < r:
                tripleSum = nums[i] + nums[l] + nums[r]

                if tripleSum < 0:
                    l += 1
                    while nums[l] == nums[l - 1]:
                        l += 1
                elif tripleSum > 0:
                    r -= 1
                    while nums[r] == nums[r + 1]:
                        r -= 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    print(l)
                    l += 1
                    while (l < len(nums) - 1) and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while nums[r] == nums[r + 1] and r > i:
                        r -= 1
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        return res