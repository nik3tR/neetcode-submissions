class Solution:
    def findMin(self, nums: List[int]) -> int:
        mins = float('inf')

        for num in nums:
            if num < mins:
                mins = num

        return mins