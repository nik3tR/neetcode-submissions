class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        return -1


# mid = 0 + (5 - 0 // 2 ) = 2
# mid = 20 + (20 // 2) = 30
# 20 - 40

# [1, 2, 3, 4, 5]

# mid = (5 - 0) //2 = 2
# if target < 3
# r = 2
# mid = (2 - 0) // 2 = 1
# target < 2 FALSE
# return mid = 1