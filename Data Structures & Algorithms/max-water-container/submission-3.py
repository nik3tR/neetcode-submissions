class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maximum = 0

        while l < r:
            minHeight = min(heights[l], heights[r])
            water = (r - l) * minHeight
            maximum = max(water, maximum)
            
            if minHeight == heights[r]:
                r -= 1
            else: l += 1
        
        return maximum