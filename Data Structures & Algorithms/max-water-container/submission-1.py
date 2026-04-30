class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l = 0;
        r = len(heights) - 1
        while l < r:
            area = 0
            if (heights[l] < heights[r]):
                area = heights[l] * (r-l)
                l += 1
            else:
                area = heights[r] * (r-l)
                r -= 1
            
            if area > largest:
                largest = area
        return largest
