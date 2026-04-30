class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        m = (l + r) // 2
        mins = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                mins = min(mins, nums[l])
                break

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
            mins = min(mins, nums[m])
            m = (l + r) // 2
            print(m, l, r)
        return mins
# 5 6 1 2 3 4
#     lr 
# 